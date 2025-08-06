# TSD-ID: SSD-4
# Filename: demo_data_to_story_brief.py
# Purpose: To provide a clear, simplified demonstration of the methodology for
#          translating quantitative data into a structured, human-centric narrative
#          brief. This serves as the technical appendix for the
#          "Case-Study-Data-To-Impact-Stories" portfolio piece.

import json

# --- INPUT DATA ---
# In a real-world scenario, this would be a key performance indicator (KPI)
# from a dashboard or analytics report.
STATISTIC = "Monthly active supporters increased by 15% in Q3."

# --- CONFIGURATION ---
# This represents the "house style" or strategic messaging guidelines that
# ensure the generated narrative aligns with organizational goals.
GUIDANCE_PRINCIPLES = [
    "Focus on the supporter's journey.",
    "Frame challenges as opportunities for engagement.",
    "Highlight the direct impact of our work."
]

def generate_story_brief(statistic, guidance):
    """
    Orchestrates the translation of a data point into a story brief.

    This function represents the core methodology of the case study: moving beyond
    simply reporting a number to interpreting its underlying human meaning and
    structuring that meaning into a brief for a creative team.

    Args:
        statistic (str): The raw data point.
        guidance (list): A list of strategic principles.

    Returns:
        dict: A structured dictionary representing the story brief.
    """

    # --- STEP 1: DATA ANALYSIS & INFERENCE ---
    # The first step is to "ask why." We move from the "what" (the statistic) to
    # the "so what?" by inferring the human story behind the number. This
    # simulates an analyst or an AI interpreting the data's meaning.
    print("Step 1: Analyzing statistic to infer narrative elements...")
    
    inferred_elements = _infer_narrative_from_statistic(statistic)
    
    print("  -> Inferred Goal:", inferred_elements['human_goal'])
    print("  -> Inferred Obstacle:", inferred_elements['obstacle'])
    print("  -> Inferred Impact:", inferred_elements['impact'])
    print("\n")


    # --- STEP 2: STRUCTURED BRIEF GENERATION ---
    # The final step is to assemble these inferred narrative elements into a
    # structured, predictable format. A JSON object or dictionary is ideal as it
    # creates a clear, machine-readable contract between the data team and the
    # creative team. The guidance principles would inform an LLM's tone and focus
    # in a real-world scenario.
    print("Step 2: Assembling elements into a final structured story brief...")
    
    story_brief = {
        "source_statistic": statistic,
        "guidance_applied": guidance,
        "narrative_brief": {
            "human_goal": inferred_elements['human_goal'],
            "obstacle": inferred_elements['obstacle'],
            "impact": inferred_elements['impact']
        }
    }
    print("  -> Brief generation complete.\n")
    
    return story_brief

def _infer_narrative_from_statistic(statistic):
    """
    A simplified simulation of an analytical or LLM-based inference step.
    
    This function looks for keywords in the statistic to deduce the core
    components of a simple story: a goal, a challenge, and a result.
    """
    # This is a simple, rule-based simulation. A real implementation would use
    # a more sophisticated NLP model or a call to an LLM.
    human_goal = "To grow our community of active supporters"
    obstacle = "Supporters were previously unengaged or unaware of opportunities."
    impact = "More people are now actively participating in our mission."

    if "decreased" in statistic.lower():
        human_goal = "To re-engage our supporter base"
        obstacle = "Recent events or lack of outreach caused a drop in engagement."
        impact = "We need a new strategy to win back our supporters' attention."
        
    return {"human_goal": human_goal, "obstacle": obstacle, "impact": impact}


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("--- Starting Data-to-Story Brief Generator ---\n")
    
    final_brief = generate_story_brief(STATISTIC, GUIDANCE_PRINCIPLES)
    
    print("--- Script Complete ---\n")
    
    print("Final Generated Story Brief (JSON format):")
    print("-------------------------------------------")
    # Use json.dumps for a clean, nicely formatted JSON output.
    print(json.dumps(final_brief, indent=2))
