# Manual Testing Plan for Jarvis Assistant

## 1️⃣ Environment Setup

- Ensure Docker is installed and running.
- Pull the latest image from Docker Hub:
    ```bash
    docker pull ayusht45cyber/jarvis-assistant:latest
    ```
- Run the container interactively:
    ```bash
    docker run -it --rm ayusht45cyber/jarvis-assistant
    ```
- Verify logs to check if services start without errors.

---

## 2️⃣ Functional Testing

| **Test Case**                         | **Steps**                              | **Expected Outcome**                                         |
|---------------------------------------|----------------------------------------|-------------------------------------------------------------|
| **Basic Speech Output**               | Run `client.py` inside the container   | Assistant responds with "Hello from Jarvis"                  |
| **Text-to-Speech (TTS) - gTTS**       | Use gTTS to convert text to speech     | Audio output is generated without errors                     |
| **Text-to-Speech (TTS) - pyttsx3**    | Use pyttsx3 to generate speech         | Text is spoken aloud correctly                               |
| **Response to Invalid Commands**     | Provide an invalid command            | Assistant handles errors gracefully                         |
| **Docker Image Size Check**           | Run `docker images | grep jarvis-assistant` | Image size is within expected range                          |

---

## 3️⃣ Performance Testing

| **Test Case**                         | **Steps**                                      | **Expected Outcome**                                |
|---------------------------------------|------------------------------------------------|----------------------------------------------------|
| **Container Startup Time**           | Measure startup time from `docker run` to readiness | Should be <5 seconds                                |
| **Memory Usage**                     | Monitor `docker stats`                         | Memory usage stays within expected limits          |
| **CPU Usage**                        | Execute multiple TTS requests                  | No excessive CPU spikes or crashes                 |

---

## 4️⃣ Security Testing

| **Test Case**                         | **Steps**                                      | **Expected Outcome**                                |
|---------------------------------------|------------------------------------------------|----------------------------------------------------|
| **Docker Security Scan**             | Run `docker scan ayusht45cyber/jarvis-assistant` | No critical vulnerabilities found                  |
| **Environment Variables Security**   | Check `.env` and logs for exposed credentials  | No credentials should be visible                   |
| **Container Isolation**              | Attempt to access host filesystem from the container | Access to the host filesystem should be restricted |

---

## 5️⃣ Usability Testing

| **Test Case**                         | **Steps**                                      | **Expected Outcome**                                |
|---------------------------------------|------------------------------------------------|----------------------------------------------------|
| **User-Friendly Responses**          | Run `client.py` with various queries           | Responses are clear and easy to understand         |
| **Error Messages Clarity**           | Provide incorrect inputs                       | Errors should be informative, not vague            |
