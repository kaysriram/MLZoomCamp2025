
FROM agrigorev/zoomcamp-model:2025

WORKDIR /app

COPY pyproject.toml .

# Install uv and dependencies, including scikit-learn explicitly
RUN pip install uv \
    && uv pip compile pyproject.toml --quiet -o requirements.txt \
    && uv pip install --system -r requirements.txt \
    && pip install fastapi uvicorn scikit-learn

# Copy your app and model
COPY predict.py .
COPY pipeline_v1.bin .

EXPOSE 8000

CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]




