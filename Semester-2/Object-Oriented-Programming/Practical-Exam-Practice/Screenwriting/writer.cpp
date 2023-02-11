#include "writer.h"
#include <sstream>

Writer::Writer()
{
    this->name = "";
    this->expertise = "";
}

Writer::Writer(std::string n, std::string e) : name{ n }, expertise{ e } {}

std::string Writer::getName() const
{
	return this->name;
}

std::string Writer::getExpertise() const
{
	return this->expertise;
}

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
//std::istream& operator>>(std::istream& is, Writer& w)
//{
//    std::string line;
//    std::getline(is, line);
//    if (line.empty())
//        return is;
//    std::vector<std::string> tokens;
//    tokens = tokenize(line, ',');
//    w.name = tokens[0];
//    w.expertise = tokens[1];
//    return is;
//}
