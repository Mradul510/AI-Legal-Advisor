package com.lawbotie.ai_legal_advisor_backend.dto;

import jakarta.validation.constraints.NotBlank;
import lombok.Data;

@Data
public class ChatRequest {
    @NotBlank(message = "Message is required")
    private String message;

    private String sessionId;
}
