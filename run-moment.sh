# Deploy with docker on Linux:
docker run \
	--name myvllm \
	-v ~/.cache/huggingface:/root/.cache/huggingface \
 	--env "HUGGING_FACE_HUB_TOKEN=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" \
	-p 8000:8000 \
	--ipc=host \
	vllm/vllm-openai:latest \
	--model AutonLab/MOMENT-1-large

#--runtime amd --gpus all \
# docker exec -it my_vllm_container bash -c "vllm serve AutonLab/MOMENT-1-large"
