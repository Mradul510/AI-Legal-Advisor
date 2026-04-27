package com.lawbotie.ai_legal_advisor_backend.controller;

import com.lawbotie.ai_legal_advisor_backend.dto.ChatRequest;
import com.lawbotie.ai_legal_advisor_backend.dto.ChatResponse;
import com.lawbotie.ai_legal_advisor_backend.entity.ChatMessage;
import com.lawbotie.ai_legal_advisor_backend.entity.ChatSession;
import com.lawbotie.ai_legal_advisor_backend.entity.User;
import com.lawbotie.ai_legal_advisor_backend.service.ChatService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/chat")
public class ChatController {

    private final ChatService chatService;

    public ChatController(ChatService chatService) {
        this.chatService = chatService;
    }

    @PostMapping
    public ResponseEntity<ChatResponse> sendMessage(
            @Valid @RequestBody ChatRequest request,
            Authentication authentication) {

        User user = (User) authentication.getPrincipal();
        ChatResponse response = chatService.processMessage(
                request.getMessage(),
                request.getSessionId(),
                user
        );
        return ResponseEntity.ok(response);
    }

    @GetMapping("/sessions")
    public ResponseEntity<List<Map<String, Object>>> getSessions(Authentication authentication) {
        User user = (User) authentication.getPrincipal();
        List<ChatSession> sessions = chatService.getUserSessions(user.getId());

        List<Map<String, Object>> sessionList = sessions.stream().map(s -> Map.<String, Object>of(
                "sessionId", s.getSessionId(),
                "title", s.getTitle() != null ? s.getTitle() : "New Chat",
                "createdAt", s.getCreatedAt().toString(),
                "updatedAt", s.getUpdatedAt().toString()
        )).toList();

        return ResponseEntity.ok(sessionList);
    }

    @GetMapping("/sessions/{sessionId}")
    public ResponseEntity<List<Map<String, Object>>> getSessionMessages(
            @PathVariable String sessionId) {

        List<ChatMessage> messages = chatService.getSessionMessages(sessionId);

        List<Map<String, Object>> messageList = messages.stream().map(m -> Map.<String, Object>of(
                "id", m.getId(),
                "content", m.getContent(),
                "isAi", m.getIsAi(),
                "category", m.getCategory() != null ? m.getCategory() : "",
                "createdAt", m.getCreatedAt().toString()
        )).toList();

        return ResponseEntity.ok(messageList);
    }
}
