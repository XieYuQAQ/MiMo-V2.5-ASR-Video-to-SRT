"""
视频/音频转字幕 Web 应用
纯浏览器端处理（FFmpeg.wasm），后端仅做 API 代理
"""

import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

MIMO_API_URL = "https://api.xiaomimimo.com/v1/chat/completions"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/recognize", methods=["POST"])
def recognize():
    """代理 MiMo ASR API 调用（避免浏览器 CORS 限制）"""
    data = request.get_json()

    audio_base64 = data.get("audio_base64", "")
    api_key = data.get("api_key", "")
    language = data.get("language", "auto")

    if not audio_base64 or not api_key:
        return jsonify({"error": "缺少参数"}), 400

    payload = {
        "model": "mimo-v2.5-asr",
        "messages": [{
            "role": "user",
            "content": [{
                "type": "input_audio",
                "input_audio": {
                    "data": f"data:audio/wav;base64,{audio_base64}"
                }
            }]
        }],
        "asr_options": {"language": language}
    }

    headers = {
        "api-key": api_key,
        "Content-Type": "application/json"
    }

    try:
        resp = requests.post(MIMO_API_URL, json=payload, headers=headers, timeout=60)

        if resp.status_code == 429:
            return jsonify({"error": "请求频率限制，请稍后重试"}), 429

        if resp.status_code != 200:
            error_msg = resp.json().get("error", {}).get("message", f"API 错误: {resp.status_code}")
            return jsonify({"error": error_msg}), resp.status_code

        result = resp.json()
        text = result["choices"][0]["message"]["content"].strip()
        return jsonify({"text": text})

    except requests.exceptions.Timeout:
        return jsonify({"error": "API 请求超时"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("=" * 50, flush=True)
    print("视频/音频转字幕 (纯浏览器版)", flush=True)
    print("打开浏览器访问: http://localhost:5000", flush=True)
    print("=" * 50, flush=True)
    app.run(debug=False, host="0.0.0.0", port=5000)
