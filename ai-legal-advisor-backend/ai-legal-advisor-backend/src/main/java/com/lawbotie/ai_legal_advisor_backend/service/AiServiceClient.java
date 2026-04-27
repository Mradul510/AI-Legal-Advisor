package com.lawbotie.ai_legal_advisor_backend.service;

import com.lawbotie.ai_legal_advisor_backend.dto.ChatResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.*;

import java.util.Map;
import java.util.HashMap;

@Service
public class AiServiceClient {

    @Value("${ai.service.url}")
    private String aiServiceUrl;

    private final RestTemplate restTemplate;

    public AiServiceClient() {
        this.restTemplate = new RestTemplate();
    }

    /**
     * Send a chat message to the Python FastAPI AI service and get back
     * the NLP response with viseme data for lip sync.
     */
    @SuppressWarnings("unchecked")
    public ChatResponse chat(String message, String sessionId) {
        String url = aiServiceUrl + "/api/chat";

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        Map<String, String> body = new HashMap<>();
        body.put("message", message);
        if (sessionId != null) {
            body.put("session_id", sessionId);
        }

        HttpEntity<Map<String, String>> request = new HttpEntity<>(body, headers);

        try {
            ResponseEntity<Map> response = restTemplate.exchange(
                    url, HttpMethod.POST, request, Map.class
            );

            Map<String, Object> data = response.getBody();
            if (data == null) {
                throw new RuntimeException("Empty response from AI service");
            }

            return ChatResponse.builder()
                    .response((String) data.get("response"))
                    .category((String) data.get("category"))
                    .categoryName((String) data.get("category_name"))
                    .confidence(data.get("confidence") != null ? ((Number) data.get("confidence")).doubleValue() : 0.0)
                    .intent((String) data.get("intent"))
                    .entities(mapEntities(data.get("entities")))
                    .keyActs((java.util.List<String>) data.get("key_acts"))
                    .tips((java.util.List<String>) data.get("tips"))
                    .visemes(mapVisemes(data.get("visemes")))
                    .morphTargets((java.util.List<Map<String, Double>>) data.get("morph_targets"))
                    .build();

        } catch (Exception e) {
            // Fallback response when AI service is unavailable
            return ChatResponse.builder()
                    .response("I apologize, but the AI service is currently unavailable. " +
                              "Please try again in a moment. For urgent legal matters, " +
                              "please consult a qualified advocate directly.")
                    .category("general")
                    .categoryName("General")
                    .confidence(0.0)
                    .intent("error")
                    .entities(java.util.Collections.emptyList())
                    .keyActs(java.util.Collections.emptyList())
                    .tips(java.util.Collections.emptyList())
                    .visemes(java.util.Collections.emptyList())
                    .morphTargets(java.util.Collections.emptyList())
                    .build();
        }
    }

    @SuppressWarnings("unchecked")
    private java.util.List<ChatResponse.EntityData> mapEntities(Object entitiesObj) {
        if (entitiesObj == null) return java.util.Collections.emptyList();
        java.util.List<Map<String, Object>> entities = (java.util.List<Map<String, Object>>) entitiesObj;
        return entities.stream().map(e -> new ChatResponse.EntityData(
                (String) e.get("text"),
                (String) e.get("label"),
                ((Number) e.get("start")).intValue(),
                ((Number) e.get("end")).intValue()
        )).toList();
    }

    @SuppressWarnings("unchecked")
    private java.util.List<ChatResponse.VisemeData> mapVisemes(Object visemesObj) {
        if (visemesObj == null) return java.util.Collections.emptyList();
        java.util.List<Map<String, Object>> visemes = (java.util.List<Map<String, Object>>) visemesObj;
        return visemes.stream().map(v -> new ChatResponse.VisemeData(
                ((Number) v.get("time")).intValue(),
                ((Number) v.get("viseme_id")).intValue(),
                (String) v.get("viseme_name"),
                ((Number) v.get("duration")).intValue()
        )).toList();
    }
}
