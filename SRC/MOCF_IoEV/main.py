from mocf_ioev.individual_charging import run_individual
from mocf_ioev.aggregated_charging import run_aggregated
from mocf_ioev.communication_model import run_communication


def main():
    print("MOCF-IoEVs Framework Running...\n")

    run_individual()
    run_aggregated()
    run_communication()


if __name__ == "__main__":
    main()
