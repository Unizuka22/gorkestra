import { useState, useEffect } from "react";

export default function GorkestraDemo() {
  const [beat, setBeat] = useState(0);
  
  useEffect(() => {
    const interval = setInterval(() => setBeat(b => (b + 1) % 4), 600);
    return () => clearInterval(interval);
  }, []);

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
      <div style={{
        background: "#0f0f17",
        border: "1px solid #ff2d7833",
        borderRadius: "12px",
        padding: "24px 32px",
        maxWidth: "520px",
        width: "100%",
        boxShadow: "0 0 40px #ff2d7815"
      }}>
        <div style={{ display: "flex", gap: "8px", marginBottom: "16px" }}>
          {["#ff5f57", "#febc2e", "#28c840"].map((c, i) => (
            <div key={i} style={{ width: 12, height: 12, borderRadius: "50%", background: c }} />
          ))}
          <span style={{ color: "#ffffff30", fontSize: "12px", marginLeft: "8px" }}>terminal</span>
        </div>
        
        <div style={{ fontFamily: "Courier New", fontSize: "13px", lineHeight: "1.8" }}>
          <div>
            <span style={{ color: "#00f5d4" }}>$</span>{" "}
            <span style={{ color: "#fff" }}>pip install gorkestra</span>
          </div>
          <div style={{ color: "#ffffff50", marginBottom: "12px" }}>
            Successfully installed gorkestra-0.1.0
          </div>
          <div>
            <span style={{ color: "#00f5d4" }}>$</span>{" "}
            <span style={{ color: "#fff" }}>gorkestra "explain recursion" --persona oracle --iq 35</span>
          </div>
          <div style={{ marginTop: "8px", color: "#ff2d78" }}>
            🎼 conducting [oracle] via openai (IQ=35)...
          </div>
          <div style={{ marginTop: "8px", color: "#e2e2e2", fontStyle: "italic" }}>
            To understand recursion, you must first understand recursion.<br />
            The scrolls say nothing more. They never did.<br />
            Go back to the beginning. You know what you did.
          </div>
        </div>
      </div>
      
      <div style={{ display: "flex", gap: "10px", flexWrap: "wrap", justifyContent: "center" }}>
        {["default", "roast", "ceo", "cope", "oracle"].map((p, i) => (
          <div
            key={p}
            style={{
              padding: "6px 16px",
              borderRadius: "999px",
              border: "1px solid",
              borderColor: ["#ff2d78", "#00f5d4", "#ffd700", "#ff8c00", "#a855f7"][i],
              color: ["#ff2d78", "#00f5d4", "#ffd700", "#ff8c00", "#a855f7"][i],
              fontSize: "12px",
              fontFamily: "Courier New",
            }}
          >
            --persona {p}
          </div>
        ))}
      </div>
    </div>
  );
}
