conscious_theory = {
      "Global Workspace Theory (GWT)": [
            {
                  "name": "Global Workspace Theory (GWT)",
                  "theory": 'qwt'
            }
      ],
      "Integrated Information Theory": [
            {
                  "name": "Integrated Information Theory",
                  "theory": "qwer"
            }
      ],
      "High-Order Thought Theory": [
            {
                  "name": "High-Order Thought Theory",
                  "theory": "qwer"
            }
      ],
      "Bayesian Brain Theory": [
            {
                  "name": "Bayesian Brain Theory",
                  "theory": "er"
            }
      ],
      "Attention Schema Theory": [
            {
                  "name": "Attention Schema Theory",
                  "theory": "qwer"
            }
      ],
      "Quantum Consciousness": [
            {
                  "name": "Quantum Consciousness",
                  "theory": "gwenchana"
            }
      ]
}

def get_conscious(conscious_thought: str):
      for category in conscious_theory.values():
            for consciousness in category:
                  if consciousness["name"].lower() == conscious_thought.lower():
                        return consciousness
      return None