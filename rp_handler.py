import runpod
from comfyui_serverless import ComfyUIHandler

handler = ComfyUIHandler()

runpod.serverless.start(
    handler=handler.handler,
    return_aggregate_stream=False
)