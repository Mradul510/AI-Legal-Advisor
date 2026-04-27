package com.lawbotie.ai_legal_advisor_backend.service;

import com.lawbotie.ai_legal_advisor_backend.dto.ChatResponse;
import com.lawbotie.ai_legal_advisor_backend.entity.ChatMessage;
import com.lawbotie.ai_legal_advisor_backend.entity.ChatSession;
import com.lawbotie.ai_legal_advisor_backend.entity.User;
import com.lawbotie.ai_legal_advisor_backend.repository.ChatMessageRepository;
import com.lawbotie.ai_legal_advisor_backend.repository.ChatSessionRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.UUID;

@Service
public class ChatService {

    private final ChatSessionRepository chatSessionRepository;
    private final ChatMessageRepository chatMessageRepository;
    private final AiServiceClient aiServiceClient;

    public ChatService(ChatSessionRepository chatSessionRepository,
                       ChatMessageRepository chatMessageRepository,
                       AiServiceClient aiServiceClient) {
        this.chatSessionRepository = chatSessionRepository;
        this.chatMessageRepository = chatMessageRepository;
        this.aiServiceClient = aiServiceClient;
    }

    public ChatResponse processMessage(String message, String sessionId, User user) {
        // Get or create session
        final String finalSessionId;
        ChatSession session;
        if (sessionId != null && !sessionId.isEmpty()) {
            finalSessionId = sessionId;
            session = chatSessionRepository.findBySessionId(finalSessionId)
                    .orElseGet(() -> createNewSession(user, finalSessionId));
        } else {
            finalSessionId = UUID.randomUUID().toString();
            session = createNewSession(user, finalSessionId);
        }

        // Save user message
        ChatMessage userMessage = ChatMessage.builder()
                .content(message)
                .isAi(false)
                .chatSession(session)
                .build();
        chatMessageRepository.save(userMessage);

        // Get AI response from Python service
        ChatResponse aiResponse = aiServiceClient.chat(message, finalSessionId);

        // Save AI response
        ChatMessage aiMessage = ChatMessage.builder()
                .content(aiResponse.getResponse())
                .isAi(true)
                .category(aiResponse.getCategory())
                .confidence(aiResponse.getConfidence())
                .intent(aiResponse.getIntent())
                .chatSession(session)
                .build();
        chatMessageRepository.save(aiMessage);

        // Update session title based on first message
        if (session.getTitle() == null || session.getTitle().isEmpty()) {
            String title = message.length() > 50 ? message.substring(0, 50) + "..." : message;
            session.setTitle(title);
            chatSessionRepository.save(session);
        }

        // Set metadata
        aiResponse.setSessionId(finalSessionId);
        aiResponse.setTimestamp(LocalDateTime.now().format(DateTimeFormatter.ofPattern("hh:mm a")));

        return aiResponse;
    }

    public List<ChatSession> getUserSessions(Long userId) {
        return chatSessionRepository.findByUserIdOrderByUpdatedAtDesc(userId);
    }

    public List<ChatMessage> getSessionMessages(String sessionId) {
        ChatSession session = chatSessionRepository.findBySessionId(sessionId)
                .orElseThrow(() -> new RuntimeException("Session not found"));
        return chatMessageRepository.findByChatSessionIdOrderByCreatedAtAsc(session.getId());
    }

    private ChatSession createNewSession(User user, String sessionId) {
        ChatSession session = ChatSession.builder()
                .sessionId(sessionId)
                .user(user)
                .build();
        return chatSessionRepository.save(session);
    }
}
