package view;

import java.util.Map;
import java.util.HashMap;
import java.util.Scanner;

public class TextMenu {

    private Map<String, Command> commands;

    public TextMenu() {
        commands = new HashMap<String, Command>();
    }

    public void addCommand(Command c) {
        commands.put(c.getKey(), c);
    }

    private void printMenu() {
        for (Command com: commands.values()) {
            String line = String.format("%4s:%s", com.getKey(), com.getDescription());
            System.out.println(line);
        }
    }

    public void show() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            printMenu();
            System.out.println("Input the option: ");
            String key = scanner.nextLine();
            Command com = commands.get(key);
            if (com == null) {
                System.out.println("Invalid option");
                continue;
            }
            com.execute();
        }
    }
}
