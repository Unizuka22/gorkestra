import { useState, useEffect } from "react";

export default function GorkestraLogo() {
  const [beat, setBeat] = useState(0);
  
  useEffect(() => {
    const interval = setInterval(() => setBeat(b => (b + 1) % 4), 600);
    return () => clearInterval(interval);
  }, []);
  
  const noteOffsets = [0, -8, -4, -12];
  
  return (
    <div style={{
      minHeight: "100vh",
      background: "#0a0a0f",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      fontFamily: "'Courier New', monospace",
      gap: "32px",
      padding: "40px"
    }}>
      <svg width="420" height="300" viewBox="0 0 420 300">
        <defs>
          <radialGradient id="glow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="#ff2d78" stopOpacity="0.15" />
            <stop offset="100%" stopColor="#0a0a0f" stopOpacity="0" />
          </radialGradient>
        </defs>
        
        <ellipse cx="210" cy="150" rx="180" ry="130" fill="url(#glow)" />
        
        {[80, 100, 120, 140, 160].map((y, i) => (
          <line key={i} x1="30" y1={y} x2="390" y2={y} stroke="#ff2d78" strokeWidth="1.5" strokeOpacity="0.3" />
        ))}
        
        <g transform={`rotate(${-20 + beat * 5}, 80, 220)`} style={{ transition: "transform 0.3s ease" }}>
          <line x1="80" y1="220" x2="145" y2="80" stroke="#00f5d4" strokeWidth="3" strokeLinecap="round" />
          <g transform="translate(145, 65)">
            <ellipse cx="0" cy="8" rx="14" ry="10" fill="#FFD700" />
            <circle cx="0" cy="-2" r="8" fill="#FFD700" />
            <ellipse cx="10" cy="-1" rx="5" ry="3" fill="#FF8C00" />
            <circle cx="4" cy="-4" r="1.5" fill="#0a0a0f" />
          </g>
        </g>
        
        {[
          { x: 180, baseY: 95, char: "♩" },
          { x: 230, baseY: 115, char: "♪" },
          { x: 280, baseY: 90, char: "♫" },
          { x: 330, baseY: 105, char: "♬" },
        ].map((note, i) => (
          <text
            key={i}
            x={note.x}
            y={note.baseY + (i === beat ? noteOffsets[i] : 0)}
            fontSize="28"
            fill={i === beat ? "#ff2d78" : "#00f5d4"}
            fillOpacity={i === beat ? 1 : 0.4}
            style={{ transition: "all 0.3s ease", userSelect: "none" }}
          >
            {note.char}
          </text>
        ))}
        
        <text x="210" y="215" textAnchor="middle" fontSize="52" fontWeight="900" letterSpacing="-2" fill="white" fontFamily="'Courier New', monospace">
          gorkestra
        </text>
        
        <text x="210" y="245" textAnchor="middle" fontSize="13" fill="#ff2d78" fontFamily="'Courier New', monospace" letterSpacing="3">
          CONDUCT YOUR AI. IT WILL NOT LISTEN.
        </text>
        
        <rect x="155" y="260" width="100" height="22" rx="11" fill="#ff2d78" fillOpacity="0.15" stroke="#ff2d78" strokeWidth="1" strokeOpacity="0.5" />
        <text x="205" y="275" textAnchor="middle" fontSize="11" fill="#ff2d78" fontFamily="'Courier New', monospace">
          v0.1.0 · MIT
        </text>
      </svg>
    </div>
  );
}
