#include "equation.h"
#include <vector>
#include <sstream>

Equation::Equation()
{
    this->a = 0;
    this->b = 0;
    this->c = 0;
}

Equation::Equation(double a, double b, double c)
{
    this->a = a;
    this->b = b;
    this->c = c;
}

double Equation::getA() const
{
    return this->a;
}

double Equation::getB() const
{
    return this->b;
}

double Equation::getC() const
{
    return this->c;
}

double Equation::getDet() const
{
    double det = b * b - 4 * a * c;
    return det;
}

std::string Equation::toString()
{
    if (this->b < 0 && this->c < 0) {
        return std::to_string(this->a) + "*x^2 " + std::to_string(this->b) + "*x " + std::to_string(this->c);
    }
    else if (this->b < 0) {
        return std::to_string(this->a) + "*x^2 " + std::to_string(this->b) + "*x + " + std::to_string(this->c);
    }
    else if (this->c < 0) {
        return std::to_string(this->a) + "*x^2 + " + std::to_string(this->b) + "*x " + std::to_string(this->c);
    }
    return std::to_string(this->a) + "*x^2 + " + std::to_string(this->b) + "*x + " + std::to_string(this->c);
}

std::vector<std::string> tokenize(const std::string& str, char delimiter)
{
    std::vector<std::string> result;
    std::stringstream ss(str);
    std::string token;
    while (getline(ss, token, delimiter))
    {
        result.push_back(token);
    }
    return result;
}


std::istream& operator>>(std::istream& reader, Equation& eq)
{
    std::string line;
    std::getline(reader, line);
    if (line.empty())
    {
        return reader;
    }
    std::vector<std::string> tokens;
    tokens = tokenize(line, ',');
    eq.a = std::stod(tokens[0]);
    eq.b = std::stod(tokens[1]); 
    eq.c = std::stod(tokens[2]);
    return reader;
}
