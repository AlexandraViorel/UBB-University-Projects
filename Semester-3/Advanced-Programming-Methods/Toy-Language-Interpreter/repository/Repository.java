package repository;

import model.MyException;
import model.PrgState;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

public class Repository implements IRepository{
    private List<PrgState> programStates;
    private String logFilePath;

    public Repository(List<PrgState> programStates, String logFilePath) {
        this.programStates = programStates;
        this.logFilePath = logFilePath;
    }

    public String getLogFilePath() {
        return logFilePath;
    }

    public void setLogFilePath(String logFilePath) {
        this.logFilePath = logFilePath;
    }

    @Override
    public void logPrgStateExec(PrgState prgState) throws MyException {
        try {
            PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
            logFile.write(prgState.toString());
            logFile.close();
        }
        catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }

    @Override
    public List<PrgState> getPrgList() {
        return this.programStates;
    }

    @Override
    public void setPrgList(List<PrgState> l) {
        this.programStates = l;
    }
}
