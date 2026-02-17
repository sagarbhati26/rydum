'use client';

import { useState } from 'react';
import { Play, Download, Music, Sliders } from 'lucide-react';

export default function Home() {
  const [bpm, setBpm] = useState(120);
  const [bars, setBars] = useState(4);
  const [style, setStyle] = useState('basic_rock');
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/api/v1/beats/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ bpm, bars, style }),
      });

      if (!response.ok) throw new Error('Generation failed');

      // Handle file download
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `beat_${style}_${bpm}bpm.mid`;
      document.body.appendChild(a);
      a.click();
      a.remove();
    } catch (error) {
      console.error(error);
      alert('Failed to generate beat. Is the backend running?');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-stone-950 text-stone-100 flex flex-col items-center justify-center p-8 font-sans">
      <div className="w-full max-w-md space-y-8">
        <div className="text-center space-y-2">
          <h1 className="text-4xl font-bold tracking-tighter text-amber-500">RYDUM</h1>
          <p className="text-stone-400">Rhythm Intelligence Platform</p>
        </div>

        <div className="bg-stone-900 border border-stone-800 rounded-2xl p-8 space-y-8 shadow-2xl">
          {/* BPM Slider */}
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <label className="text-sm font-medium text-stone-300 flex items-center gap-2">
                <Music size={16} /> BPM
              </label>
              <span className="text-xl font-mono text-amber-500">{bpm}</span>
            </div>
            <input
              type="range"
              min="60"
              max="180"
              value={bpm}
              onChange={(e) => setBpm(Number(e.target.value))}
              className="w-full h-2 bg-stone-800 rounded-lg appearance-none cursor-pointer accent-amber-500"
            />
          </div>

          {/* Bars Slider */}
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <label className="text-sm font-medium text-stone-300 flex items-center gap-2">
                <Sliders size={16} /> Bars
              </label>
              <span className="text-xl font-mono text-amber-500">{bars}</span>
            </div>
            <input
              type="range"
              min="1"
              max="8"
              value={bars}
              onChange={(e) => setBars(Number(e.target.value))}
              className="w-full h-2 bg-stone-800 rounded-lg appearance-none cursor-pointer accent-amber-500"
            />
          </div>

          {/* Style Selection */}
          <div className="space-y-4">
            <label className="text-sm font-medium text-stone-300">Style</label>
            <div className="grid grid-cols-3 gap-2">
              {['basic_rock', 'house', 'hiphop'].map((s) => (
                <button
                  key={s}
                  onClick={() => setStyle(s)}
                  className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${style === s
                    ? 'bg-amber-500 text-stone-950'
                    : 'bg-stone-800 text-stone-400 hover:bg-stone-700'
                    }`}
                >
                  {s.replace('_', ' ').toUpperCase()}
                </button>
              ))}
            </div>
          </div>

          {/* Generate Button */}
          <button
            onClick={handleGenerate}
            disabled={loading}
            className="w-full py-4 bg-stone-100 text-stone-950 rounded-xl font-bold text-lg hover:bg-white active:scale-95 transition-all flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? (
              'Generating...'
            ) : (
              <>
                <Download size={20} /> Generate MIDI
              </>
            )}
          </button>
        </div>
      </div>
    </main>
  );
}
