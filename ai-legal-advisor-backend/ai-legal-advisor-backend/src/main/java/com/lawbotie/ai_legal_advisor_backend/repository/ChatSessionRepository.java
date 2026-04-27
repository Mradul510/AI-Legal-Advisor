package com.lawbotie.ai_legal_advisor_backend.repository;

import com.lawbotie.ai_legal_advisor_backend.entity.ChatSession;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface ChatSessionRepository extends JpaRepository<ChatSession, Long> {
    List<ChatSession> findByUserIdOrderByUpdatedAtDesc(Long userId);
    Optional<ChatSession> findBySessionId(String sessionId);
}
