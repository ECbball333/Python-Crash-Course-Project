
import printing_models

unprinted_designs = ['car', 'truck']
completed_models = []


current_design = unprinted_designs.pop()
completed_models.append(current_design)

printing_models.show_completed_models( completed_models)