#pragma once
#include <vector>
#include <algorithm>

class Observer {
public:
	virtual void update() = 0;
	virtual ~Observer() {}
};

class Observable {
private:
	std::vector<Observer*> observers;

public:
	void addObserver(Observer* obs) {
		this->observers.push_back(obs);
	}

	void removeObserver(Observer* obs) {
		auto it = std::find(this->observers.begin(), this->observers.end(), obs);
		if (it != this->observers.end())
			this->observers.erase(it);
	}

	void notify() {
		for (auto o : this->observers) {
			o->update();
		}
	}
	virtual ~Observable() {}
};