#!/usr/bin/env python3
"""
Airdrop Scoring System
Score and filter airdrops based on legitimacy and ROI potential
"""

import json
from datetime import datetime

AIRDROP_CHECKLIST = {
    "must_have": [
        "known_team",           # Doxxed or known team members
        "active_development",   # Recent GitHub commits
        "real_product",         # Working product or testnet
        "no_kyc_required",      # No identity verification needed
        "no_deposit_required",  # No money to participate
        "verified_contracts",   # Smart contracts verified
    ],
    "good_to_have": [
        "vc_backed",           # Venture capital backing
        "large_community",     # 10k+ Discord/Twitter
        "token_launched",      # Already has token (lower risk)
        "mainnet_live",        # Mainnet deployed
        "partnerships",        # Known partnerships
    ],
    "red_flags": [
        "requires_deposit",
        "requires_kyc",
        "anonymous_team",
        "no_product",
        "guaranteed_returns",
        "referral_focused",
        "no_github",
        "low_liquidity",
    ]
}

def score_airdrop(airdrop_data):
    """Score an airdrop 0-100"""
    score = 0
    reasons = []
    
    # Must-have checks (50 points)
    for check in AIRDROP_CHECKLIST["must_have"]:
        if airdrop_data.get(check):
            score += 50 // len(AIRDROP_CHECKLIST["must_have"])
        else:
            reasons.append(f"Missing: {check}")
    
    # Good-to-have checks (30 points)
    for check in AIRDROP_CHECKLIST["good_to_have"]:
        if airdrop_data.get(check):
            score += 30 // len(AIRDROP_CHECKLIST["good_to_have"])
    
    # Red flag penalties (-20 each)
    for flag in AIRDROP_CHECKLIST["red_flags"]:
        if airdrop_data.get(flag):
            score -= 20
            reasons.append(f"Red flag: {flag}")
    
    return max(0, min(100, score)), reasons

# Curated airdrop list (high quality only)
CURRENT_AIRDROPS = [
    {
        "name": "Monetrix",
        "url": "https://airdrops.io/monetrix/",
        "chain": "Ethereum",
        "score": 85,
        "type": "DeFi",
        "tasks": ["Connect wallet", "Follow X", "Join TG/Discord", "Share post"],
        "vc_backed": True,
        "active_development": True,
        "no_kyc": True,
        "no_deposit": True,
        "notes": "Claim Pioneer SBT"
    },
    {
        "name": "ChainGPT",
        "url": "https://airdrops.io/chaingpt/",
        "chain": "Solana",
        "score": 80,
        "type": "AI",
        "tasks": ["Connect EVM wallet", "Provide Solana address", "Register", "Post about DeCharge", "Follow X"],
        "vc_backed": True,
        "active_development": True,
        "no_kyc": True,
        "no_deposit": True,
        "notes": "$150K giveaway, create content for $CHARGE tokens"
    },
    {
        "name": "DogeOS",
        "url": "https://airdrops.io/dogeos/",
        "chain": "Dogechain",
        "score": 75,
        "type": "GameFi",
        "tasks": ["Connect wallet", "Link X", "Follow X", "Connect TG", "Join Discord", "Assemble crew"],
        "vc_backed": False,
        "active_development": True,
        "no_kyc": True,
        "no_deposit": True,
        "notes": "GameFi airdrop"
    },
    {
        "name": "ForeGate",
        "url": "https://airdrops.io/foregate/",
        "chain": "Solana",
        "score": 70,
        "type": "Prediction",
        "tasks": ["Predict", "Complete tasks"],
        "vc_backed": False,
        "active_development": True,
        "no_kyc": True,
        "no_deposit": True,
        "notes": "Prediction market"
    },
    {
        "name": "Grass",
        "url": "https://airdrops.io/grass/",
        "chain": "Solana",
        "score": 90,
        "type": "DePIN",
        "tasks": ["Install desktop app", "Run node", "Connect Solana wallet"],
        "vc_backed": True,
        "active_development": True,
        "no_kyc": True,
        "no_deposit": True,
        "notes": "Stage 2 running, install app to earn points"
    }
]

def main():
    print("🎯 Airdrop Scoring Results")
    print("=" * 60)
    
    for airdrop in sorted(CURRENT_AIRDROPS, key=lambda x: x["score"], reverse=True):
        status = "🟢" if airdrop["score"] >= 75 else "🟡" if airdrop["score"] >= 50 else "🔴"
        print(f"\n{status} {airdrop['name']} ({airdrop['chain']}) — Score: {airdrop['score']}/100")
        print(f"   Type: {airdrop['type']}")
        print(f"   Tasks: {', '.join(airdrop['tasks'])}")
        print(f"   Notes: {airdrop['notes']}")
        print(f"   URL: {airdrop['url']}")

if __name__ == "__main__":
    main()
