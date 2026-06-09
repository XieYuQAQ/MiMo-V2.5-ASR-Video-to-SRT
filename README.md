# MiMo-V2.5-ASR 视频/音频转字幕工具

基于 MiMo-V2.5-ASR 语音识别模型，支持从视频/音频文件中提取音频并自动生成 SRT 字幕文件。纯浏览器端处理，无需安装任何软件。

## 在线使用

访问 [GitHub Pages 地址](https://xieyuqaq.github.io/MiMo-V2.5-ASR-Video-to-SRT/) 即可使用。

## 特性

- 纯浏览器端处理，音频提取由 FFmpeg.wasm 完成
- 支持视频格式：MP4、MKV、AVI、MOV、WebM
- 支持音频格式：MP3、WAV、FLAC、AAC、OGG、M4A
- 自动按固定时长切片，逐段识别
- 识别语言支持：中文、英文、自动检测
- 生成标准 SRT 字幕文件，可直接下载
- API Key 本地保存，无需重复输入

## 使用方法

1. 在设置区填入你的 MiMo API Key（从 [MiMo 开放平台](https://platform.xiaomimimo.com) 获取）
2. 选择识别语言（默认自动检测）
3. 拖拽或点击上传视频/音频文件
4. 点击「开始处理」
5. 等待处理完成，预览字幕内容
6. 点击「下载 SRT 字幕文件」

## 文件结构

```
public/
├── index.html              # 主页面
├── README.md               # 本文档
└── static/
    └── ffmpeg/             # FFmpeg.wasm 文件（约 30MB）
        ├── ffmpeg.js
        ├── ffmpeg-core.js
        ├── ffmpeg-core.wasm
        └── 814.ffmpeg.js
```

## 工作原理

```
浏览器端（FFmpeg.wasm）
├── 读取上传的视频/音频文件
├── 提取音频（WAV 16kHz 单声道）
├── 按 15 秒切片
└── 逐段 Base64 编码

浏览器端（JavaScript）
├── 调用 MiMo API 识别每段音频
├── 拼接识别结果
└── 生成 SRT 字幕并提供下载
```

## 前置条件

- 现代浏览器（Chrome / Edge / Firefox / Safari）
- MiMo API Key

## 许可

本项目仅用于学习和个人使用。语音识别服务由 [Xiaomi MiMo](https://platform.xiaomimimo.com) 提供。

---

> 本项目使用 mimo-v2.5-pro 编写。
