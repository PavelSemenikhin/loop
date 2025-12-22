from base64 import b64encode

steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]


for step in steps:
    print(b64encode(step.encode("utf-8")).decode("utf-8"))
