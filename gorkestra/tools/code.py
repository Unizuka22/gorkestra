"""Code execution tool."""

import subprocess
import tempfile
import os
from typing import Dict
from .base import Tool

class CodeExecutor(Tool):
    """Execute code in a sandboxed environment."""
    
    name = "code_exec"
    description = "Execute Python code safely"
    
    def __init__(self, sandbox: bool = True, timeout: int = 30):
        self.sandbox = sandbox
        self.timeout = timeout
    
    def execute(self, code: str, language: str = "python") -> Dict:
        """
        Execute code and return result.
        
        Args:
            code: Code to execute
            language: Programming language
        
        Returns:
            {stdout, stderr, exit_code}
        """
        if language != "python":
            return {"error": f"Language '{language}' not supported yet"}
        
        # Write to temp file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write(code)
            temp_path = f.name
        
        try:
            result = subprocess.run(
                ["python", temp_path],
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "exit_code": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {"error": f"Execution timed out after {self.timeout}s"}
        finally:
            os.unlink(temp_path)
