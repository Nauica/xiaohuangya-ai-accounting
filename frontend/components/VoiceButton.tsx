import React, { useState, useEffect } from 'react';
import { Button } from 'react-native'; // 或 import { Button } from 'react-native-paper';
import Voice from '@react-native-voice/voice';

export default function VoiceButton() {
  const [isRecording, setIsRecording] = useState(false);

  // 初始化语音监听
  useEffect(() => {
    const onSpeechResults = (e: any) => {
      const text = e.value?.[0] || '';
      fetch('http://localhost:5000/parse', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ speech: text }),
      }); // 发送到后端解析
    };

    Voice.onSpeechResults = onSpeechResults;

    return () => {
      Voice.destroy().then(Voice.removeAllListeners);
    };
  }, []);

  const startRecording = async () => {
    await Voice.start('zh-CN'); // 中文识别
    setIsRecording(true);
  };

  const stopRecording = async () => {
    await Voice.stop();
    setIsRecording(false);
  };
  

  return (
    <Button 
      title={isRecording ? "识别中..." : "语音记账"} 
      onPress={isRecording ? stopRecording : startRecording}
    />
  );
}