package Day5;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Objects;

public class Day5 {
    ArrayList<int[]> instructions;
    String[][] crates;
    public void doInstructions() {
        for (int[] instr : instructions) {
            int from = instr[1] -1;
            int to = instr[2]-1;
            int i = instr[0];
            while (i > 0) {
                makeMoveOneAtaTime(from, to);
                i--;
            }
        }
    }

    public void doInstructions2() {
        for (int[] instr : instructions) {
            int from = instr[1] -1;
            int to = instr[2]-1;
            int i = instr[0];
            makeMoveMultiple(i, from, to);
        }
    }
    public int getTopIndex(int col) {
        for (int i = 0; i < 199; i++) {
            if (crates[i][col].contains("[")) {
                return i;
            }
        }
        return 199;
    }
    public void makeMoveOneAtaTime(int from, int to) {
        int rowfrom = getTopIndex(from);
        int rowto = getTopIndex(to) - 1;
        crates[rowto][to] = crates[rowfrom][from];
        crates[rowfrom][from] = "    ";
    }

    public void makeMoveMultiple(int homany, int from, int to) {
        int rowfrom = getTopIndex(from) + homany - 1;
        int rowto = getTopIndex(to) - 1;
        for (int i = 0; i < homany; i++) {
            crates[rowto-i][to] = crates[rowfrom-i][from];
            crates[rowfrom-i][from] = "    ";
        }
    }
    public static void main(String[] args) {
        Day5 d = new Day5();
        BufferedReader reader;
        d.instructions = new ArrayList<>();
        boolean instruct = false;
        d.crates = new String[200][9];
        for(int i = 0; i < 200; i++) {
            for(int j = 0; j < 9; j++) {
                d.crates[i][j] = "    ";
            }
        }
        File input = new File("Day5/input");
        try {
            reader = new BufferedReader(new FileReader(input));
            String line = reader.readLine();
            int j = 192;
            String[] characters = line.split("(?<=\\G....)");
            for (int i = 0; i < characters.length; i++) {
                if (!characters[i].equals("")) {
                    d.crates[j][i] = characters[i];
                }
            }
            j++;
            line = reader.readLine();
            while (line != null) {
                if (!instruct) {
                    if (line.contains("1")) {
                        reader.readLine();
                        instruct = true;
                    } else {
                        characters = line.split("(?<=\\G....)");
                        for (int i = 0; i < characters.length; i++) {
                            if (!characters[i].equals("")) {
                                d.crates[j][i] = characters[i];
                            }
                        }
                        j++;
                    }
                } else {
                    String better = line.replaceAll("[^0-9]", " ");
                    better = better.replaceAll(" +", " ");
                    String[] numbers = better.split(" ");
                    int[] temp = new int[3];
                    for (int i = 1; i < 4; i++) {
                        temp[i-1] = Integer.parseInt(String.valueOf(numbers[i]));
                    }
                    d.instructions.add(temp);
                }
                line = reader.readLine();
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        //d.doInstructions();
        d.doInstructions2();
        System.out.println(d.toString());
    }

    @Override
    public String toString() {
        String result = "";
        for (String[] row : crates) {
            for (String chars : row) {
                result += chars;
            }
            result += "\n";
        }
        return result;
    }
}
