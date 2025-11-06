{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO3APalY4FutMRf6YrCgrGc",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Anifowak/ScRNA-Seq-Analysis-HackBio-Internship-2025/blob/main/simple_code.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GN68X1Lxnyuw",
        "outputId": "ec7abd8b-65f9-44f6-f18e-35b224297ad4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "HackBio Team Aspartic Information:\n",
            "\n",
            "\n",
            "HackBio Team Aspartic Information:\n",
            "\n",
            "Name                          Slack Username           Country        Hobby               Affiliation                                  Fav Gene  Sequence\n",
            "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n",
            "Funmilayo                     Funmilayo Ligali         Nigeria        Cooking             Biochemistry                                 TP53      ATGGAGGAGCCGCAGTCAGAT\n",
            "Akinjide                      Akinjide Anifowose       Nigeria        Coding              Biomedical Informatics                       PTEN      ATGACAGCCATCATCAAAGAG\n",
            "Fakhia Mubashir               Fakhia Mubashir          Pakistan       Reading             None                                         TRPV6     ATCGTCGCCCGATACGATCCAGTA\n",
            "Niraj Pun Magar               Niraj Pun Magar          Nepal          UX design           Bioinformatics                               APOE      ATGCATGCGCGCATGC\n",
            "Himanshu Pundir               Himanshu Pundir          India          Editing             Bioinformatics                               SIR1      ATGTCTATAAAAGGAAAT\n",
            "Diksha Shetty                 Diksha Shetty            India          Reading             Bioinformatics                               MYC       GGAGTTTATTCATAACGCGCTCTCCAAGTATACGTGGCAATGCGTT\n",
            "Sri Sathya Sandilya Garemilla Garemilla Sandilya       United States  Coding              Bioinformatics and Molecular Biochemistry    NIL       AACCGCATCTGCAGCGAGCATCTGAGAAGCCAAGACTGAGCCGGCGGCCGCGGCGCAGCGAACGAGCAGT\n",
            "\n",
            "Total_team_members: 7\n"
          ]
        }
      ],
      "source": [
        "\"\"\"\n",
        "HackBio Internship - Stage 0 Python Task\n",
        "Team: Aspartic\n",
        "\n",
        "# Task: Write a simple Python script for printing the names, slack username, country, 1 hobby, affiliations of people on your team and the DNA sequence of the genes they love most.\n",
        "# Author: Funmilayo Christianah Ligali\n",
        "# GitHub: https://github.com/Christianah001\n",
        "# LinkedIn: https://www.linkedin.com/in/funmilayo-ligali-9746a2184/\n",
        "\"\"\"\n",
        "\n",
        "# Team information stored in a list of dictionaries\n",
        "# Each dictionary represents one member\n",
        "team_aspartic_info = [\n",
        "        {\"Name\": \"Funmilayo\", \"Slack\": \"Funmilayo Ligali\", \"Country\": \"Nigeria\", \"Hobby\": \"Cooking\",\n",
        "     \"Affiliation\": \"Biochemistry\", \"Favorite Gene\": \"TP53\", \"Sequence\": \"ATGGAGGAGCCGCAGTCAGAT\"},\n",
        "    {\"Name\": \"Akinjide\", \"Slack\": \"Akinjide Anifowose\", \"Country\": \"Nigeria\", \"Hobby\": \"Coding\",\n",
        "     \"Affiliation\": \"Biomedical Informatics\", \"Favorite Gene\": \"PTEN\", \"Sequence\": \"ATGACAGCCATCATCAAAGAG\"},\n",
        "    {\"Name\": \"Fakhia Mubashir\", \"Slack\": \"Fakhia Mubashir\", \"Country\": \"Pakistan\", \"Hobby\": \"Reading\",\n",
        "     \"Affiliation\": \"None\", \"Favorite Gene\": \"TRPV6\", \"Sequence\": \"ATCGTCGCCCGATACGATCCAGTA\"},\n",
        "    {\"Name\": \"Niraj Pun Magar\", \"Slack\": \"Niraj Pun Magar\", \"Country\": \"Nepal\", \"Hobby\": \"UX design\",\n",
        "     \"Affiliation\": \"Bioinformatics\", \"Favorite Gene\": \"APOE\", \"Sequence\": \"ATGCATGCGCGCATGC\"},\n",
        "    {\"Name\": \"Himanshu Pundir\", \"Slack\": \"Himanshu Pundir\", \"Country\": \"India\", \"Hobby\": \"Editing\",\n",
        "     \"Affiliation\": \"Bioinformatics\", \"Favorite Gene\": \"SIR1\", \"Sequence\": \"ATGTCTATAAAAGGAAAT\"},\n",
        "    {\"Name\": \"Diksha Shetty\", \"Slack\": \"Diksha Shetty\", \"Country\": \"India\", \"Hobby\": \"Reading\",\n",
        "     \"Affiliation\": \"Bioinformatics\", \"Favorite Gene\": \"MYC\", \"Sequence\": \"GGAGTTTATTCATAACGCGCTCTCCAAGTATACGTGGCAATGCGTT\"},\n",
        "    {\"Name\": \"Sri Sathya Sandilya Garemilla\", \"Slack\": \"Garemilla Sandilya\", \"Country\": \"United States\", \"Hobby\": \"Coding\",\n",
        "     \"Affiliation\": \"Bioinformatics and Molecular Biochemistry\", \"Favorite Gene\": \"NIL\", \"Sequence\": \"AACCGCATCTGCAGCGAGCATCTGAGAAGCCAAGACTGAGCCGGCGGCCGCGGCGCAGCGAACGAGCAGT\"},\n",
        "]\n",
        "\n",
        "# To define a simple function to print member details\n",
        "def print_member(member):\n",
        "    \"\"\"Prints formatted details of a team member.\"\"\"\n",
        "    print(f\"{member['Name']:<30}{member['Slack']:<25}{member['Country']:<15}\"\n",
        "          f\"{member['Hobby']:<20}{member['Affiliation']:<45}\"\n",
        "          f\"{member['Favorite Gene']:<10}{member['Sequence']}\")\n",
        "\n",
        "# To print a title\n",
        "print(\"\\nHackBio Team Aspartic Information:\\n\")\n",
        "\n",
        "# To print header for clarity\n",
        "print(\"\\nHackBio Team Aspartic Information:\\n\")\n",
        "print(f\"{'Name':<30}{'Slack Username':<25}{'Country':<15}\"\n",
        "      f\"{'Hobby':<20}{'Affiliation':<45}\"\n",
        "      f\"{'Fav Gene':<10}{'Sequence'}\")\n",
        "print(\"-\" * 170)\n",
        "\n",
        "# Loop through team members and print each one\n",
        "for member in team_aspartic_info:\n",
        "    print_member(member)\n",
        "\n",
        "# To print total team members\n",
        "print(f\"\\nTotal_team_members: {len(team_aspartic_info)}\")"
      ]
    }
  ]
}