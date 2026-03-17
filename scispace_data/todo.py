Planner Code plan:
```python
def main():
    # 1. Search for Tier 1: Birdsong crystallization, Gallistel conditioning, Rodent maze, and Primate/Corvid insight.
    # Focus on individual trajectories, step functions, and longitudinal data.
    search_scholarly_literature(query="individual zebra finch song development trajectory Sound Analysis Pro Tchernichovski abrupt transition")
    search_scholarly_literature(query="Gallistel individual learning curve step function abrupt transition conditioning change point detection")
    search_scholarly_literature(query="Reddy 2022 PNAS mouse labyrinth individual path efficiency discontinuous learning")
    search_scholarly_literature(query="Corvid primate insight problem solving individual trial performance trajectory Kohler Bird Emery")

    # 2. Search for Tier 2 & 3: Mooney images, Human AGL, Honeybee concepts, Vocabulary explosion, and Neural transitions.
    search_scholarly_literature(query="Mooney image recognition perceptual learning individual subject data hysteresis")
    search_scholarly_literature(query="artificial grammar learning implicit learning individual trajectory sudden improvement")
    search_scholarly_literature(query="honeybee concept learning individual performance transition Giurfa Avargues-Weber")
    search_scholarly_literature(query="vocabulary explosion child language development individual trajectory longitudinal naming spurt")
    search_scholarly_literature(query="Durstewitz prefrontal neural ensemble abrupt transition rule learning individual trial data")

    # 3. Download PDFs for high-relevance papers identified in search results (prioritizing those mentioning individual data/trajectories).
    # bulk_fulltext_download() will be used for papers found via search.

    # 4. Analyze the downloaded PDFs to verify if they meet the criteria:
    # - Individual-level trajectories?
    # - Time series of performance?
    # - Raw data/digitizable figures available?
    # - N >= 5 individuals, >= 20 time points?
    scispace_ask_question_on_multiple_files(
        questions=[
            "Does this paper provide individual learning trajectories or just group means?",
            "Is there a time series of performance (accuracy, latency, similarity) over trials or days?",
            "Is the raw data available in supplementary materials or an open repository? Are the figures high-quality and digitizable?",
            "How many individuals are included and how many time points are there per individual?"
        ],
        pdf_paths=["/home/sandbox/paper1.pdf", "..."] # List of paths from previous step
    )

    # 5. Search for open data repositories related to animal and human learning to find raw datasets directly.
    activate_skill(skill_name="web-search-and-scrape")
    web_search(query="animal learning open data repository individual trial conditioning birdsong maze insight behavioral")

    # 6. Synthesize all findings into a comprehensive research report.
    # The report will categorize evidence by species/domain, highlight "Must-Have" sources, and flag papers with usable data/figures.
    write_report(
        topic="Discontinuous Learning Transitions Across Species: A Review of Individual Trajectories and Data Availability",
        instructions="Synthesize the literature search and PDF analysis. Categorize by the requested tiers (Birdsong, Conditioning, Maze, Insight, etc.). Explicitly flag sources with downloadable data or digitizable figures. Include citations for all classic and modern studies found."
    )

if __name__ == "__main__":
    main()
```