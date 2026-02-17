"""Tõlgi (väljasta ekraanile) järgmised sõnad:

    tere -> inglise k, itaalia k
    auto -> itaalia k
    kass - > inglise k
    üks -> itaalia k
    kolm -> inglise k """

from _01_inglise_itaalia import est_eng_dict, est_ita_dict
est_ita_dict["üks"] = "uno"
est_ita_dict["kolm"] = "tre"
est_eng_dict["üks"] = "one"
est_eng_dict["kolm"] = "three"


if __name__ == "__main__":
    print(f"Tere -> inglise keeles: {est_eng_dict["tere"]}, itaalia keeles: {est_ita_dict["tere"]}")
    print(f"auto -> itaalia keeles: {est_ita_dict["auto"]}")
    print(f"kass -> inglise keeles: {est_eng_dict["kass"]}")
    print(f"üks -> itaalia keeles: {est_ita_dict["üks"]}")
    print(f"kolm -> inglise keeles: {est_eng_dict["kolm"]}")

