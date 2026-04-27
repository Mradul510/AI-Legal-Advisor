package com.lawbotie.ai_legal_advisor_backend.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class AuthResponse {
    private String token;
    private String name;
    private String email;
    private Long userId;
    private String referralCode;
    private Integer referralCount;
}
