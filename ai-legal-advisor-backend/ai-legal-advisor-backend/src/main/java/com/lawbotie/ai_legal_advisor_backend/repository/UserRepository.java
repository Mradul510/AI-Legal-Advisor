package com.lawbotie.ai_legal_advisor_backend.repository;

import com.lawbotie.ai_legal_advisor_backend.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
    boolean existsByEmail(String email);
    Optional<User> findByReferralCode(String referralCode);
}
