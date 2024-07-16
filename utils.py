import nrrd

"""
Classe para cada paciente, contém o id, o caminho para o ficheiro acom as imagens, 
o scan(pylidc) e os nódulos que são uma lista com as anotações.
"""
class Patient:

    def __init__(self, idx, dicom_file, scan, nods):

        self.idx = idx
        self.dicom_file = dicom_file
        self.scan = scan
        self.nods = nods


"""
Função para guardar as imagens e a malignancy de cada anotação.
Uma anotação é um objeto da classe annotation da biblioteca pylidc, logo é recomendado 
que se consulte a documentação desta biblioteca para se perceber melhor como funcionam
algumas das funções usadas (https://pylidc.github.io/).
"""
def get_nrrd_images(ann, i, annotation_folder):

    vol = ann.scan.to_volume()
    padding = [(30,10), (10,25), (0,0)]

    mask = 1*(ann.boolean_mask(pad=padding))
    bbox = ann.bbox(pad=padding)

    image_path = f"{annotation_folder}/image.nrrd"
    mask_path = f"{annotation_folder}/mask.nrrd"
    maligancy_path = f"{annotation_folder}/malignancy.txt"

    nrrd.write(mask_path, mask)
    nrrd.write(image_path, vol[bbox])

    f = open(maligancy_path, "x")
    f.write(f"{ann.malignancy}")
    f.close()
    



