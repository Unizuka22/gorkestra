"""X (Twitter) integration for posting and engagement."""

import os
from typing import Optional, List, Dict
from .base import Tool

class XClient(Tool):
    """Post and interact on X/Twitter."""
    
    name = "x_post"
    description = "Post to X (Twitter)"
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        access_token: Optional[str] = None,
        access_secret: Optional[str] = None
    ):
        self.api_key = api_key or os.getenv("X_API_KEY")
        self.api_secret = api_secret or os.getenv("X_API_SECRET")
        self.access_token = access_token or os.getenv("X_ACCESS_TOKEN")
        self.access_secret = access_secret or os.getenv("X_ACCESS_SECRET")
        self._client = None
    
    @property
    def client(self):
        if self._client is None:
            try:
                import tweepy
                auth = tweepy.OAuth1UserHandler(
                    self.api_key,
                    self.api_secret,
                    self.access_token,
                    self.access_secret
                )
                self._client = tweepy.API(auth)
            except ImportError:
                raise ImportError("tweepy required: pip install tweepy")
        return self._client
    
    def execute(self, action: str = "post", **kwargs) -> Dict:
        """Execute X action."""
        if action == "post":
            return self.post(kwargs.get("text", ""))
        elif action == "thread":
            return self.thread(kwargs.get("tweets", []))
        elif action == "reply":
            return self.reply(kwargs.get("tweet_id"), kwargs.get("text"))
        else:
            return {"error": f"Unknown action: {action}"}
    
    def post(self, text: str) -> Dict:
        """Post a tweet."""
        if len(text) > 280:
            return {"error": "Tweet exceeds 280 characters"}
        
        try:
            tweet = self.client.update_status(text)
            return {
                "success": True,
                "id": tweet.id_str,
                "url": f"https://x.com/i/status/{tweet.id_str}"
            }
        except Exception as e:
            return {"error": str(e)}
    
    def thread(self, tweets: List[str]) -> Dict:
        """Post a thread."""
        results = []
        reply_to = None
        
        for i, text in enumerate(tweets):
            try:
                if reply_to:
                    tweet = self.client.update_status(
                        text,
                        in_reply_to_status_id=reply_to
                    )
                else:
                    tweet = self.client.update_status(text)
                
                reply_to = tweet.id
                results.append({
                    "index": i,
                    "id": tweet.id_str,
                    "success": True
                })
            except Exception as e:
                results.append({
                    "index": i,
                    "error": str(e),
                    "success": False
                })
        
        return {"thread": results}
    
    def reply(self, tweet_id: str, text: str) -> Dict:
        """Reply to a tweet."""
        try:
            tweet = self.client.update_status(
                text,
                in_reply_to_status_id=tweet_id
            )
            return {"success": True, "id": tweet.id_str}
        except Exception as e:
            return {"error": str(e)}
