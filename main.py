from assets import GradingAssistant, rubric


def main():
    rubric_data = rubric("assets/sep_of_proteins_2_3.json")
    assistant = GradingAssistant(rubric_data)
    assistant.iterate_over_dictionary(assistant.rubric_dict)
    assistant.summarize()
    # assistant.debug()
    
if __name__ == "__main__":
    main()