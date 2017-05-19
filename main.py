import query
import sys
import actions


def main():
    command = 8
    connect = query.connect_db()
    while command > 0 and command <= 8:
        command = query.display_menu()
        connect = query.connect_db()
        if command == 1:
            actions.display_mentors_name(connect)
        elif command == 2:
            actions.display_nicknames(connect)
        elif command == 3:
            actions.carols_data(connect)
        elif command == 4:
            actions.hat_owner(connect)
        elif command == 5:
            actions.update_jemima(connect)
        elif command == 6:
            actions.delete_arsenio_and_friend(connect)
        elif command == 7:
            sys.exit
    command = int(8)

if __name__ == '__main__':
    main()