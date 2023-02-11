#pragma once
#include "service.h"
#include "userService.h"

class UI {
private:
	Service& adminService;
	UserService& userService;

	/// <summary>
	/// This function handles adding a dog. It is used in administrator mode.
	/// </summary>
	void handleAdd();

	/// <summary>
	/// This function handles removing a dog. It is used in administrator mode.
	/// </summary>
	void handleRemove();

	/// <summary>
	/// This function handles updating a dog. It is used in administrator mode.
	/// </summary>
	void handleUpdate();

	/// <summary>
	/// This function prints the dogs from the administrator repository.
	/// </summary>
	void printDogs();

	/// <summary>
	/// This function prints the dogs from the adopting list.
	/// </summary>
	void printAdoptingList();

	/// <summary>
	/// This function handles adopting dogs by displaying all dogs from the repository.
	/// </summary>
	void handleAdoptAll();

	/// <summary>
	/// This function handles adopting dogs by displaying a filtered list of dogs of a given breed
	/// and having an age less than the given age.
	/// </summary>
	void handleAdoptFiltered();

	/// <summary>
	/// This function opens the adopting list from the CSV/HTML file.
	/// </summary>
	void openFile();

	/// <summary>
	/// This function displays the administrator mode menu.
	/// </summary>
	void displayAdminMenu();

	/// <summary>
	/// This function displays the user mode menu.
	/// </summary>
	void displayUserMenu();

public:
	/// <summary>
	/// Constructor for the UI.
	/// </summary>
	/// <param name="adminService">: the administrator mode service</param>
	/// <param name="userService">: the user mode service</param>
	UI(Service& adminService, UserService& userService);

	/// <summary>
	/// This function starts the application.
	/// </summary>
	void run();

	/// Destructor.
	~UI();
};