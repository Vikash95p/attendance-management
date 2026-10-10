from ai_model import inference_client


request = {
    "action": "check_attendance",
    "roll_no": "CS001",
    "date": "2026-10-10"
}


response = inference_client(request)


print("AI Response:")
print(response)