try:
    import json_file_handler 
except ModuleNotFoundError:
    print("Error: The 'json_file_handler' module is not found.")
    exit()

data = json_file_handler.read_json_file(
    "insulin.json"
)

if data:
    b_insulin = data["molecules"][
        "bInsulin"
    ] 
    a_insulin = data["molecules"][
        "aInsulin"
    ]  
    insulin = b_insulin + a_insulin  

    molecular_weight_insulin_actual = data[
        "molecularWeightInsulinActual"
    ]  
    print("bInsulin: " + b_insulin)  
    print("aInsulin: " + a_insulin)  
    print(
        "molecularWeightInsulinActual: " + str(molecular_weight_insulin_actual)
    )  

    aa_weights = data["weights"]  

    aa_count_insulin = {x: float(insulin.upper().count(x)) for x in aa_weights.keys()}

    molecular_weight_insulin = sum(
        {x: (aa_count_insulin[x] * aa_weights[x]) for x in aa_weights.keys()}.values()
    )
    
    print(
        "The rough molecular weight of insulin: " + str(molecular_weight_insulin)
    )  
    print(
        "Percent error: "
        + str(
            (
                (molecular_weight_insulin - molecular_weight_insulin_actual)
                / molecular_weight_insulin_actual
            )
            * 100
        )
    )
else:
    print("Error. Exiting program") 
