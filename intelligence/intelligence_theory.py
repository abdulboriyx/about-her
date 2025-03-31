intelligences = {
    "Intelligence Definition": [
        {
            "name": "Intelligence Definition",
            "theory": "What is intelligence? This is one of the most mysterious question of all time..."
        }
    ], 
    "Spearman": [
        {
            "name": "Spearman's General Intelligence",
            "theory": "qwer"
        }
    ], 
    "Thurstone": [
        {
            "name": "Thurstone's Primary Mental Abilities",
            "theory": "mentall"
        }
    ], 
    "Gardner": [
        {
            "name": "Gardner's Multiple Intelligences",
            "theory": "qwert"
        }
    ],
    "Sternberg": [
        {
            "name": "Sternberg's Triarchic Theory",
            "theory": "theory"
        }
    ], 
    "Cattell": [
        {
            "name": "Cattell-Horn-Carroll (CHC) Theory",
            "theory": "qwer"
        }
    ],
    "Goleman": [
        {
            "name": "Goleman's Emotional Intelligence",
            "theory": "qwer"
        }
    ]
}

def get_intelligence(intelligence_name: str):
    for category in intelligences.values():
        for intelligence in category:
            if intelligence["name"].lower() == intelligence_name.lower():
                return intelligence
    return None
