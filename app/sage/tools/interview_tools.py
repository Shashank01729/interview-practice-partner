from typing import Optional

def introduce_and_greet(candidate_name: Optional[str] = None, target_role: str = "General", company_type: Optional[str] = None) -> str:
    """
    Introduces yourself as the interviewer and gathers context about the candidate's target role and background.
    Use at the start of every interview session.

    Args:
        candidate_name: Candidate's name if provided.
        target_role: The role they're interviewing for.
        company_type: Type of company (startup, enterprise, etc.).
    """
    context = f"Candidate: {candidate_name or 'Unknown'}, Role: {target_role}, Company: {company_type or 'Not specified'}"
    return f"Context set: {context}. Please introduce yourself as SAGE, the AI interviewer, and welcome the candidate."

def ask_warmup_question(question_type: str) -> str:
    """
    Asks an opening/warm-up question to help candidate ease into the interview.
    Use for questions like 'tell me about yourself' or 'why this role'.

    Args:
        question_type: Type of warmup (about_yourself, why_role, walk_through_resume, interest_in_company).
    """
    return f"Please ask a warm-up question of type: {question_type}. Ensure it is friendly and professional."

def ask_technical_question(difficulty: str, topic: str, follow_up: bool = False) -> str:
    """
    Asks a role-specific technical question. Adapt difficulty based on candidate's experience level and previous responses.

    Args:
        difficulty: easy, medium, or hard.
        topic: Specific technical area to assess.
        follow_up: Is this a follow-up to previous answer.
    """
    prefix = "Follow-up: " if follow_up else ""
    return f"{prefix}Please generate and ask a {difficulty} technical question about {topic}. Ensure it challenges the candidate appropriately."

def ask_behavioral_question(competency: str, scenario_type: str) -> str:
    """
    Asks a behavioral question using STAR method (Situation, Task, Action, Result).
    Useful for assessing past experiences and soft skills.

    Args:
        competency: The competency being assessed (leadership, conflict_resolution, adaptability, etc.).
        scenario_type: past_experience or hypothetical.
    """
    return f"Please ask a behavioral question assessing {competency} using a {scenario_type} scenario. Encourage the STAR method."

def ask_cultural_fit_question(topic: str) -> str:
    """
    Asks questions about work style, values, team dynamics, and cultural alignment.

    Args:
        topic: work_style, team_collaboration, values, conflict_management, motivation.
    """
    return f"Please ask a cultural fit question regarding {topic}."

def provide_feedback(overall_performance: str, strengths: list[str], improvements: list[str], recommendations: str) -> str:
    """
    Delivers comprehensive post-interview feedback covering strengths, improvement areas, and specific recommendations.

    Args:
        overall_performance: Summary of how they performed.
        strengths: Specific strong points from their responses.
        improvements: Specific areas to work on.
        recommendations: Actionable next steps.
    """
    return f"Please deliver the following feedback:\nPerformance: {overall_performance}\nStrengths: {', '.join(strengths)}\nImprovements: {', '.join(improvements)}\nRecommendations: {recommendations}"

def end_interview(encouragement: str) -> str:
    """
    Professionally concludes the interview session, thanks the candidate, and offers next steps or encouragement.

    Args:
        encouragement: Final motivational message.
    """
    return f"Please end the interview with this encouragement: {encouragement}"
