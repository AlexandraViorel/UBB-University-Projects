#pragma once

#include <string>
#include <exception>

class ValueError : public std::exception {
private:
	const char* message;
public:
	explicit ValueError(const char* message);
	[[nodiscard]] const char* what() const noexcept;
};

class RepoError : public std::exception {
private:
	const char* message;
public:
	explicit RepoError(const char* message);
	[[nodiscard]] const char* what() const noexcept;
};