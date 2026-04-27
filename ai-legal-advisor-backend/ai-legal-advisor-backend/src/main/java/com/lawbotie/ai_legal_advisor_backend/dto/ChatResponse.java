package com.lawbotie.ai_legal_advisor_backend.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.util.List;
import java.util.Map;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class ChatResponse {
    private String response;
    private String category;
    private String categoryName;
    private Double confidence;
    private String intent;
    private List<EntityData> entities;
    private List<String> keyActs;
    private List<String> tips;
    private List<VisemeData> visemes;
    private List<Map<String, Double>> morphTargets;
    private String sessionId;
    private String timestamp;

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class EntityData {
        private String text;
        private String label;
        private int start;
        private int end;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class VisemeData {
        private int time;
        private int visemeId;
        private String visemeName;
        private int duration;
    }
}
