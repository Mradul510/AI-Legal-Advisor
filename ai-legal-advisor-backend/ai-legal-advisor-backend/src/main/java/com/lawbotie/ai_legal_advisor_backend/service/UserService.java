package com.lawbotie.ai_legal_advisor_backend.service;

import com.lawbotie.ai_legal_advisor_backend.config.JwtUtil;
import com.lawbotie.ai_legal_advisor_backend.dto.AuthResponse;
import com.lawbotie.ai_legal_advisor_backend.dto.LoginRequest;
import com.lawbotie.ai_legal_advisor_backend.dto.SignupRequest;
import com.lawbotie.ai_legal_advisor_backend.entity.User;
import com.lawbotie.ai_legal_advisor_backend.repository.UserRepository;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final JwtUtil jwtUtil;

    public UserService(UserRepository userRepository, PasswordEncoder passwordEncoder, JwtUtil jwtUtil) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
        this.jwtUtil = jwtUtil;
    }

    public AuthResponse signup(SignupRequest request) {
        if (userRepository.existsByEmail(request.getEmail())) {
            throw new RuntimeException("Email already registered");
        }

        User user = User.builder()
                .name(request.getName())
                .email(request.getEmail())
                .password(passwordEncoder.encode(request.getPassword()))
                .referralCode(generateReferralCode())
                .referralCount(0)
                .build();

        user = userRepository.save(user);
        String token = jwtUtil.generateToken(user.getEmail());

        return AuthResponse.builder()
                .token(token)
                .name(user.getName())
                .email(user.getEmail())
                .userId(user.getId())
                .referralCode(user.getReferralCode())
                .referralCount(user.getReferralCount())
                .build();
    }

    public AuthResponse login(LoginRequest request) {
        User user = userRepository.findByEmail(request.getEmail())
                .orElseThrow(() -> new RuntimeException("Invalid email or password"));

        if (!passwordEncoder.matches(request.getPassword(), user.getPassword())) {
            throw new RuntimeException("Invalid email or password");
        }

        String token = jwtUtil.generateToken(user.getEmail());

        return AuthResponse.builder()
                .token(token)
                .name(user.getName())
                .email(user.getEmail())
                .userId(user.getId())
                .referralCode(user.getReferralCode())
                .referralCount(user.getReferralCount())
                .build();
    }

    public User getUserByEmail(String email) {
        return userRepository.findByEmail(email)
                .orElseThrow(() -> new RuntimeException("User not found"));
    }

    private String generateReferralCode() {
        return "LAW-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();
    }
}
