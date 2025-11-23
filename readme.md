# Interview Practice Partner

This project is a voice agent (with chat option) application using Google's GenAI and FastAPI, designed to simulate a professional job interview experience.

## Approach & Architecture

### Single Agent, Multiple Tools
The core of this application is a **Single Agent** architecture that leverages **Multiple Tools** to drive the conversation. The agent, "SAGE", is a sophisticated LLM configured with a specific persona and a set of callable tools.

-   **Agent Persona**: SAGE acts as a Senior Technical Recruiter with 15+ years of experience.
-   **Tool-Use Strategy**: Instead of a rigid script, the agent dynamically selects tools based on the conversation context to progress through the interview stages.

### Session Management
The application uses an `InMemorySessionService` to maintain context throughout the interaction.
-   **Context Retention**: The agent remembers previous answers, allowing for deep follow-up questions and personalized feedback.
-   **State Tracking**: The session service tracks the current stage of the interview to ensure a logical flow.

## Guardrails

To ensure a safe, professional, and effective experience, the agent operates within strict guardrails:

1.  **Professionalism**: The agent maintains a professional tone, avoids discriminatory questions, and does not discuss inappropriate topics (e.g., salary expectations, personal issues).
2.  **Scope Limits**: The agent stays in character and focuses solely on interview practice. It declines requests to perform unrelated tasks (e.g., writing code, creating resumes).
3.  **Quality Control**: The agent prioritizes quality interaction over speed, adapting to the user's pace and ensuring thorough feedback.

## Interview Flow

The interview follows a structured yet adaptive flow, driven by specific tools:

1.  **`introduce_and_greet`**: The agent starts the session, establishes rapport, and gathers context (role, experience).
2.  **`ask_warmup_question`**: Light, introductory questions to get the candidate comfortable (e.g., "Tell me about yourself").
3.  **`ask_technical_question`**: Role-specific technical questions to assess hard skills and problem-solving abilities.
4.  **`ask_behavioral_question`**: STAR-method based questions to evaluate soft skills and past experiences.
5.  **`ask_cultural_fit_question`**: Questions regarding work style, values, and team dynamics.
6.  **`provide_feedback`**: Comprehensive, actionable feedback highlighting strengths and areas for improvement.
7.  **`end_interview`**: Professional closing of the session.

## Future Enhancements

We are planning to evolve the architecture to a **Multi-Agent System** for even greater capability:

-   **Multi-Agent Orchestration**: Instead of a single agent, an **Orchestrator Agent** will manage the overall session.
-   **Agent-to-Agent (A2A) Communication**:
    -   **Interviewer Agent**: Conducts the interview and asks questions.
    -   **Observer Agent**: Listens to the user's responses in real-time to analyze behavioral traits (e.g., "chatty," "efficient," "nervous") and provides cues to the Interviewer Agent.
    -   **Monitor Agent**: Oversees the process to ensure goals are met and suggests real-time improvements to the Interviewer Agent.
    -   This protocol allows agents to communicate and collaborate behind the scenes to deliver a hyper-personalized experience.

---

## Prerequisites

-   **Python 3.10 or higher**: Ensure you have Python installed. You can check with `python --version`.

## Setup

1.  **Clone or Download** the repository to your local machine.
2.  **Navigate** to the project directory in your terminal:
    ```bash
    cd interview-practice-partner
    ```

3.  **Create a Virtual Environment** (Recommended):
    ```bash
    python -m venv venv
    ```

4.  **Activate the Virtual Environment**:
    -   **Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    -   **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

## Installation

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Configuration

1.  Create a `.env` file in the root directory.
2.  Add your Google Gemini API Key:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    GOOGLE_GENAI_USE_VERTEXAI=FALSE
    ```

## Running the Application

Start the application using `uvicorn`:

```bash
python -m uvicorn app.main:app --reload
```

## Usage

1.  Open your web browser.
2.  Go to **[http://localhost:8000](http://localhost:8000)**.
3.  You should see the voice agent interface.
4.  Click on the microphone icon or the "Start" button (depending on the UI) to begin interacting with the agent.