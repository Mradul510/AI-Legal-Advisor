package com.lawbotie.ai_legal_advisor_backend.repository;

import com.lawbotie.ai_legal_advisor_backend.entity.ChatMessage;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ChatMessageRepository extends JpaRepository<ChatMessage, Long> {
    List<ChatMessage> findByChatSessionIdOrderByCreatedAtAsc(Long sessionId);
    long countByChatSessionId(Long sessionId);
}
