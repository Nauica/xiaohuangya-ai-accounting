// frontend/screens/VoiceTestScreen.js
import { useState } from 'react';
import { Button } from 'react-native-paper';
import * as Speech from 'expo-speech';

export default function VoiceTest() {
  const [text, setText] = useState("测试语音识别");
  
  const speak = () => {
    Speech.speak(text, { language: 'zh-CN' });
  };

  return <Button mode="contained" onPress={speak}>播放语音</Button>;
}