
def obter_status(status_id):
    status_map = {
        1: "Lista de espera",
        2: "A começar",
        3: "Em andamento",
        4: "Revisão",
        5: "Finalizado"
    }

    return status_map.get(status_id)