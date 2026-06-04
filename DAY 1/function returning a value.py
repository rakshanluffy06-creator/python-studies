def create_patient_id(name):
    patient_id = name[:3].upper() + "_001"
    return patient_id

id1 = create_patient_id("Priya")
print(id1)
