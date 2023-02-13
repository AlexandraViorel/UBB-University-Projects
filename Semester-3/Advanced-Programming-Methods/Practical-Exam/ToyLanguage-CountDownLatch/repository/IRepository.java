package repository;

import model.MyException;
import model.PrgState;

import java.util.List;

public interface IRepository {
    public void logPrgStateExec(PrgState p) throws MyException;

    public List<PrgState> getPrgList();

    public void setPrgList(List<PrgState> l);
}
