#include "idea.h"
#include <sstream>

Idea::Idea() : description{ "" }, status{ "" }, creator{ "" }, act{ 0 }
{
}

Idea::Idea(std::string d, std::string s, std::string c, int a) : description{ d }, status{ s }, creator{ c }, act{ a }
{
}

std::string Idea::getDescription() const
{
    return this->description;
}

std::string Idea::getStatus() const
{
    return this->status;
}

std::string Idea::getCreator() const
{
    return this->creator;
}

int Idea::getAct() const
{
    return this->act;
}
void Idea::setStatus(std::string st)
{
    this->status = st;
}
//
//std::vector<std::string> tokenize(const std::string& line, char delimiter)
//{
//    std::vector<std::string> result;
//    std::stringstream ss(line);
//    std::string token;
//    while (getline(ss, token, delimiter)) {
//        result.push_back(token);
//    }
//    return result;
//
//}
//
//std::istream& operator>>(std::istream& is, Idea& idea)
//{
//    std::string line;
//    std::getline(is, line);
//    if (line.empty()) {
//        return is;
//    }
//    std::vector<std::string> tokens;
//    tokens = tokenize(line, ',');
//    idea.description = tokens[0];
//    idea.status = tokens[1];
//    idea.creator = tokens[2];
//    idea.act = std::stoi(tokens[3]);
//    return is;
//}
