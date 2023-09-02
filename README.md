# A4AF
A4AF is a web-based tool designed to assist individuals interested in commencing or expanding their own agricultural ventures. Our customized chatbot is crafted to offer guidance, catering to both beginners and seasoned experts. Additionally, we offer pertinent training tutorials to further empower you in your journey.

## Structure
auth\
  auth.py: Cointains basic authentication implementation.
  
models\: key components of our project: ChatGPT, PestDetection, VideoRecomender, and Storage classes. These elements enable us to offer each user a distinct experience, with a special focus on ChatGPT and VideoRecomender, which deliver personalized content based on user profiles.

static\ and templates\: Here, you will find the frontend code for the A4AF platform, implemented using HTML, CSS, and JavaScript files for the user interface.

views\: This directory houses blueprints, allowing us to effectively structure and manage our routes.

## Purpose
The primary purpose of this repository is to serve as a centralized hub for our codebase, which plays a crucial role in our software development project. It provides us with a structured and organized environment where we can collectively manage, update, and enhance our code.

## How Generative AI Models are Solving the Problem
In this project, we leveraged several AI models to enhance its functionality and user experience. Here's an overview of the models used and their respective roles:

* GPT-3.5-Turbo: We employed the GPT-3.5-Turbo model as the core component of our chatbot system. This model was responsible for providing personalized responses and content based on the user's profile. It played a crucial role in creating a tailored experience for each user, offering relevant information and guidance.

* Microsoft/ResNet-50: Our project made use of the Microsoft/ResNet-50 model for the purpose of pest detection. Although this model isn't specifically trained for pest detection, it was integrated into our system to identify potential pests. However, due to the possibility of incorrect predictions, we enhanced its accuracy by cross-referencing its outputs with GPT-3.5-Turbo's insights. If pests were detected, the chatbot would subsequently offer advice on managing the issue, along with video tutorial recommendations.

* YouTube API Integration: To provide users with personalized video tutorials, we integrated the YouTube API into our system. GPT-3.5-Turbo generated relevant search strings, which were then used to search for videos tailored to the user's needs. This approach ensured that each user received personalized and instructive video content to support their specific requirements.

* Transition to meta-llama/Llama-2-70b-hf: To address the cost concerns associated with the paid GPT-3.5-Turbo model, we've made the strategic decision to transition to the meta-llama/Llama-2-70b-hf model, which is available for free. However, this transition is pending approval from both Meta and Hugging Face to grant us access to the desired model. Once approved, this transition will help us maintain the quality of our service while managing costs effectively.

By integrating these AI models and continuously working to optimize our approach, we aim to provide users with a comprehensive and personalized experience in various aspects of the project, from chatbot interactions to pest detection and video tutorial recommendations.
