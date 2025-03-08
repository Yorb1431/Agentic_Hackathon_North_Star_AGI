# Agentic Hackathon - North Star AGI

## Project Overview
**Agentic_Hackathon_North_Star_AGI** is an advanced AI-driven system designed to showcase autonomous problem-solving capabilities in dynamic environments. Created by **Angelo and Yorbe**, this project aims to push the boundaries of artificial general intelligence (AGI) through agentic interactions, real-time decision-making, and adaptive learning.

## Features
- **Autonomous Decision Making** – Implements AI agents that analyze, reason, and execute actions independently.
- **Real-Time Adaptability** – Continuously learns and refines decision-making based on new data.
- **Multi-Agent Collaboration** – Supports interactions between AI agents for problem-solving.
- **Security & Ethical AI** – Includes safeguards to ensure responsible AI behavior.

## Installation
To set up the project, follow these steps:

1. **Clone the Repository**
   ```sh
   git clone https://github.com/YOUR-REPO/Agentic_Hackathon_North_Star_AGI.git](https://github.com/Yorb1431/Agentic_Hackathon_North_Star_AGI.git)
   cd Agentic_Hackathon_North_Star_AGI
   ```

2. **Run the Application**
   ```sh
   python main.py
   ```

## Usage
- Modify `config.json` to adjust parameters for agent behaviors.
- Use `agent_interface.py` to interact with the AI agents.
- Log results and insights in `logs/` for analysis.


## Contact
For inquiries or collaborations, reach out via GitHub Issues or email.

### Project Description: Phishing Email Detector

In this project, we created a **Phishing Email Detector**, a tool designed to help users identify whether an email is a phishing attempt or not. Phishing emails are fraudulent messages that try to trick people into sharing sensitive information like passwords, credit card numbers, or personal details. This tool analyzes the content of an email and provides a score indicating how likely it is to be a phishing attempt, along with detailed warnings and analysis.

#### **What Does the Tool Do?**
The Phishing Email Detector works by scanning the text of an email for specific patterns, keywords, and links that are commonly used in phishing attempts. Here’s how it works step by step:

1. **User Input**: The user pastes the content of an email into a text box on the website.
2. **Analysis**: The tool checks the email for:
   - **Suspicious Keywords**: Words like "urgent," "password," "verify," or "account" that are often used in phishing emails.
   - **Suspicious Links**: Links that lead to known phishing websites or domains.
   - **Suspicious Sender**: Emails from addresses like "noreply" or "no-reply" that are often used in automated phishing campaigns.
3. **Scoring**: Based on the analysis, the tool calculates a **Phishing Score** (as a percentage) to indicate how suspicious the email is.
4. **Results**: The tool displays:
   - The **Phishing Score** (e.g., 25%, 50%, 75%).
   - A **Status** (e.g., "Likely Safe," "Suspicious," or "Phishing Detected").
   - **Warnings**: A list of issues found in the email (e.g., "Uses urgent language").
   - **Analysis Details**: A breakdown of what was checked, such as whether suspicious links or sensitive information requests were detected.

#### **How Did We Build It?**
We built this tool using **HTML**, **Tailwind CSS**, **JavaScript**, and integrated **DeepSeek LLM** for advanced text analysis. Here’s a breakdown of the key components:

1. **HTML**: This is the structure of the website. It includes:
   - A text box where users can paste the email content.
   - A button to start the analysis.
   - A section to display the results, including the score, status, warnings, and analysis details.

2. **Tailwind CSS**: This is a modern CSS framework that makes it easy to create beautiful, responsive designs. We used Tailwind to style the website, making it look clean and professional. For example:
   - The text box and button have a modern design with rounded corners and hover effects.
   - The results section is neatly organized with clear headings and a subtle background color to make it stand out.

3. **JavaScript**: This is the "brain" of the tool. It handles the logic for analyzing the email and calculating the score. Here’s what the JavaScript code does:
   - It checks the email for suspicious keywords, links, and sender information.
   - It calculates a score based on how many suspicious elements are found.
   - It updates the website dynamically to show the results to the user.

4. **DeepSeek LLM**: We integrated **DeepSeek LLM** (Large Language Model) to enhance the tool's ability to analyze and understand the context of the email content. DeepSeek LLM helps in:
   - Detecting more sophisticated phishing attempts by understanding the context and nuances of the email text.
   - Providing more accurate and detailed analysis, especially for emails that use advanced social engineering tactics.

#### **Key Features of the Tool**
1. **Easy to Use**: The interface is simple and user-friendly. Users just need to paste the email content and click a button to get the results.
2. **Detailed Analysis**: The tool doesn’t just give a score—it also provides a list of warnings and a breakdown of what was checked, so users can understand why an email might be suspicious.
3. **Responsive Design**: The website looks great on both desktop and mobile devices, thanks to Tailwind CSS.
4. **Dynamic Updates**: The results are displayed instantly without needing to reload the page, making the experience smooth and fast.
5. **Advanced Text Analysis**: With the integration of DeepSeek LLM, the tool can detect more sophisticated phishing attempts and provide more accurate results.

#### **How Does It Help Users?**
This tool is designed to help users protect themselves from phishing attacks. By analyzing emails and providing a clear score and warnings, it helps users:
   - **Identify Suspicious Emails**: Users can quickly see if an email is likely to be a phishing attempt.
   - **Avoid Scams**: By knowing what to look for (e.g., urgent language or suspicious links), users can avoid falling for phishing scams.
   - **Stay Safe Online**: The tool educates users about common phishing tactics, making them more aware and cautious when dealing with emails.

#### **Example Use Case**
Imagine you receive an email that says:
```
Subject: URGENT: Your Account Has Been Compromised

Dear User,

We have detected unusual activity on your account. Please click the link below to verify your login details immediately:
http://bank-security.com/verify-account

If you do not verify your account within 24 hours, your account will be temporarily suspended.

Sincerely,
The Security Team
```

You’re not sure if this email is real or a phishing attempt. You copy the email content and paste it into the Phishing Email Detector. The tool analyzes the email and gives you the following results:
   - **Phishing Score**: 75%
   - **Status**: Phishing Detected! Be careful with this email.
   - **Warnings**:
     - Uses urgent language
     - Contains suspicious links
   - **Analysis Details**:
     - Suspicious Links: Detected
     - Sensitive Info Requests: Detected
     - Urgency Language: Detected
     - Grammar/Spelling Issues: Not Detected
     - Suspicious Sender: Not Detected

Based on this analysis, you realize the email is likely a phishing attempt and avoid clicking the link or sharing any personal information.

#### **What’s Next?**
While this tool is already functional, there are several ways it could be improved in the future:
   - **Machine Learning**: Adding a machine learning model to analyze emails more accurately and detect new phishing tactics.
   - **More Features**: Adding checks for grammar and spelling mistakes, which are common in phishing emails.
   - **User Accounts**: Allowing users to save their analysis history or report phishing emails to a database.
   - **Browser Extension**: Turning the tool into a browser extension that automatically checks emails in your inbox.

#### **Conclusion**
The Phishing Email Detector is a simple yet powerful tool that helps users identify and avoid phishing emails. By combining a clean, user-friendly interface with detailed analysis and scoring, it provides valuable insights into the safety of an email. The integration of **DeepSeek LLM** enhances the tool's ability to detect sophisticated phishing attempts, making it even more effective. Whether you’re a student, professional, or just someone who wants to stay safe online, this tool is a great way to protect yourself from phishing scams.
