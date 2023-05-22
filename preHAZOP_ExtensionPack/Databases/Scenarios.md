### Pump
#### Pump for pressure 

| Index | Description                                | Guideword | Parameter | Cause_1           | Cause_2                      | Cause_3                | Consequence_1     | Consequence_2   | Consequence_3 | Danger of leakage | Safeguard_1                                               | Safeguard_2                              | References                                       |
| ----- | ------------------------------------------ | --------- | --------- | ----------------- | ---------------------------- | ---------------------- | ----------------- | --------------- | ------------- | ----------------- | --------------------------------------------------------- | ---------------------------------------- | ----------------------------------|
| 1     | Failure of the seal (general)              | Lower     | Pressure  | bearing failure   | \-                           | \-                     | leak of chemicals | \-              | \-            | Yes               | install pressure sensor                                   | install check valve in the delivery line | Kletz  [^1]                        |
| 8     | Pump damage due to high pressure (general) | Higher    | Pressure  | vaporizing liquid | blockage in the valve outlet | \-                     | explosion         | stop production |               | Yes               | check and drain pipes and drain system                    | replace the gasket and check the damage  | Youcef [^2]       |
| 9     | Pump does not work  (general)              | No        | Pressure  | pump failure      | power outage                 | faulty pressure sensor | stop production   | stop the pump   | \-            |                   | check the types of liquids that can be used with the pump | install pressure sensor                  | Youcef [^2], changed by Yang |

#### Pump for flow 
| Index | Description                                             | Guideword | Parameter | Cause_1                      | Cause_2                                    | Cause_3               | Consequence_1           | Consequence_2                    | Consequence_3 | Danger of leakage | Safeguard_1                                   | Safeguard_2                                                     | References                                                             |
| ----- | ------------------------------------------------------- | --------- | --------- | ---------------------------- | ------------------------------------------ | --------------------- | ----------------------- | -------------------------------- | ------------- | ----------------- | --------------------------------------------- | --------------------------------------------------------------- |  ----------------------------------|
| 2     | Bearing failure (general)                               | Lower     | Flow      | lack of lubrication          | \-                                         | \-                    | failure of the seal     | \-                               | \-            |                   | install pressure sensor                       | install check valve in the delivery line                        | Kletz [^1]                                                 |
| 4     | Mechanical failure of the pump (general)                | No        | Flow      | mechanical failure           | power outage                               | \-                    | damage                  | continuous process disturbed     | \-            |                   | bypass                                        | \-                                                              | Holtermann [^3]                          |
| 10    | high flow rate in the pump (general)                    | Higher    | Flow      | blockage in the valve outlet | operating fault                            | too high engine power | overheating of the pump | destruction of the internal pump | cavitation    |                   | install remotely operated valves (controlled) | check density of liquid that differens from the nominal density | Youcef [^2]                             |
| 11    | Idling of the centrifugal pump (Pump, centrifugal type) | No        | Flow      | closed discharge valve       | inlet medium of the pump is not sufficient | \-                    | overheating of the pump | mechanical damage                | cavitation    |                   | set up ldling sensing system                  | install flow sensor                                             | angroupcn.com [^5], Youcef [^2] |

#### Pump for temperature
| Index | Description                                                               | Guideword | Parameter   | Cause_1                                                | Cause_2                                   | Cause_3                        | Consequence_1                       | Consequence_2                      | Consequence_3          | Danger of leakage | Safeguard_1                | Safeguard_2                                   | References                                 |
| ----- | ------------------------------------------------------------------------- | --------- | ----------- | ------------------------------------------------------ | ----------------------------------------- | ------------------------------ | ----------------------------------- | ---------------------------------- | ---------------------- | ----------------- | -------------------------- | --------------------------------------------- | ----------------------------------|
| 3     | Pumping against wrongly closed valve results in damage of pump  (general) | Higher    | Temperature | valve wrongly closed                                   | \-                                        | \-                             | damage to the seals                 | leak of chemicals                  | \-                     | Yes               | bypass                     | install remotely operated valves (controlled) | Holtermann [^3]                   |
| 5     | Bursting of a pump (general)                                              | Higher    | Temperature | operating error, wrongly started between closed valves | pump housing made of brittle material     | operating error went unnoticed | vapor pressure of the liquid raised | pump burst                         | \-                     | Yes               | install pressure sensor    | install remotely operated valves (controlled) | DECHEMA [^4]                |
| 7     | Failure in the cooling system  (general)                                  | Lower     | Temperature | low flow rates                                         | failure in the cooling system (open more) | \-                             | fat lose its viscosity              | change of lubricant characteristic | damage to the bearings |                   | install temperature sensor | check the cooling system                      | Youcef [^2] |

#### Pump for msr
| Index | Description                                      | Guideword | Parameter | Cause_1                                                                            | Cause_2                                      | Cause_3               | Consequence_1            | Consequence_2                                                 | Consequence_3      | Danger of leakage | Safeguard_1                                                                | Safeguard_2             | References                 |
| ----- | ------------------------------------------------ | --------- | --------- | ---------------------------------------------------------------------------------- | -------------------------------------------- | --------------------- | ------------------------ | ------------------------------------------------------------- | ------------------ | ----------------- | -------------------------------------------------------------------------- | ----------------------- | -------------------------- |
| 6     | Centrifugal pump blast  (Pump, centrifugal type) | No        | MSR       | crystallization occurred and blockage of the pipeline over a longer period of time | failure of the volume flow monitoring system | no second measurement | reduction of volume flow | the organic liquid in the pipeline heated up until decomposed | the pump destroyed | Yes               | ensure the function of critical systems by second, independent measurement | install two or more MSR | DECHEMA [^4] |

### Heat exchanger
#### Heat exchanger for pressure
| Index | Description                                                                                  | Guideword | Parameter | Cause_1                                                           | Cause_2 | Cause_3 | Consequence_1                  | Consequence_2 | Consequence_3 | Danger of leakage | Safeguard_1                            | Safeguard_2                       | References                               |
| ----- | -------------------------------------------------------------------------------------------- | --------- | --------- | ----------------------------------------------------------------- | ------- | ------- | ------------------------------ | ------------- | ------------- | ----------------- | -------------------------------------- | --------------------------------- | ----------------------------------|
| 14    | More pressure on tube side of Shell&Tube Heat Exchanger (Heat exchanger with straight tubes) | Higher    | Pressure  | failure of process fluid valve                                    | \-      | \-      | bursting of tube               | \-            | \-            | Yes               | Install high pressure alarm            | \-                                | Hazard and Operability [^6]          |
| 15    | Contamination of process fluid line (general)                                                | Lower     | Pressure  | leakage of tube and cooling flow or heating flow goes in          | \-      | \-      | contamination of process fluid | \-            | \-            | Yes               | proper maintainance and operator alert | \-                                | Hazard and Operability [^6] and changed by Yang |
| 19    | Pressure shock causes leakage at plate heat exchanger (plate heat exchanger)                 | Lower     | Pressure  | a pressure surge on the product side of the plate heat exchangers | \-      | \-      | seal failure                   | \-            | \-            |                   | sealing materials must be resistant    | use shell and tube heat exchanger | DECHEMA [^4]         |

#### Heat exchanger for flow
| Index | Description                                         | Guideword | Parameter          | Cause_1                                             | Cause_2         | Cause_3 | Consequence_1                                 | Consequence_2                                 | Consequence_3 | Danger of leakage | Safeguard_1         | Safeguard_2 | References                      |
| ----- | --------------------------------------------------- | --------- | ------------------ | --------------------------------------------------- | --------------- | ------- | --------------------------------------------- | --------------------------------------------- | ------------- | ----------------- | ------------------- | ----------- | -----------------------|
| 12    | Reduced flow of heating or cooling medium (general) | Lower     | Flow               | pipe blockage                                       | wrong operation | \-      | temperature of process fluid remains constant | \-                                            | \-            | Yes               | install flow alarm  | \-          | Hazard and Operability [^6] |
| 13    | More cooling flow or heating flow (general)         | More      | Flow               | failure of cooling flow valve or heating flow valve | wrong operation | \-      | temperature of process fluid decrease         | \-                                            | \-            |                   | install flow alarm  | \-          | Hazard and Operability [^6] |
| 17    | Reverse process fluid flow (general)                | Reverse   | Process fluid flow | failure of process fluid inlet valve                | \-              | \-      | product off set                               | temperature of process fluid remains constant | \-            |                   | install check valve | \-          | Hazard and Operability [^6] |

#### Heat exchanger for temperature
| Index | Description                                                    | Guideword | Parameter   | Cause_1                                                                                       | Cause_2                                                                | Cause_3                                 | Consequence_1                | Consequence_2                                                 | Consequence_3 | Danger of leakage | Safeguard_1                           | Safeguard_2                   | References            |
| ----- | -------------------------------------------------------------- | --------- | ----------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------- | ---------------------------- | ------------------------------------------------------------- | ------------- | ----------------- | ------------------------------------- | ----------------------------- | --------------------- |
| 18    | Restarting the heat exchangerl cause brittle failure (general) | Lower     | Temperature | ice formed on the outside of the heat exchanger when the flow of warm heating medium  stopped | heat exchanger could not withstand low temperatures and thermal shocks | not clear in the operating instructions | the heat exchanger fractured | explosion because of releasing hydrocarbon vapors and liquids | \-            | Yes               | the operators need to be good trained | install low temperature alarm | Kletz [^1] |

#### Heat exchanger others
| Index | Description                                            | Guideword | Parameter | Cause_1                   | Cause_2 | Cause_3 | Consequence_1                  | Consequence_2 | Consequence_3 | Danger of leakage | Safeguard_1         | Safeguard_2 | References                      |
| ----- | ------------------------------------------------------ | --------- | --------- | ------------------------- | ------- | ------- | ------------------------------ | ------------- | ------------- | ----------------- | ------------------- | ----------- | ------------------------------- |
| 16    | Corrosion of tube (Heat exchanger with straight tubes) | Corrosion | Tube      | hardness of cooling water | \-      | \-      | less cooling and crack of tube | \-            | \-            | Yes               | proper maintainence | \-          | Hazard and Operability [^6] |

### Reactor
#### Reactor for level
| Index | Description                     | Guideword | Parameter | Cause_1             | Cause_2              | Cause_3                         | Consequence_1              | Consequence_2    | Consequence_3 | Danger of leakage | Safeguard_1                       | Safeguard_2              | References |
| ----- | ------------------------------- | --------- | --------- | ------------------- | -------------------- | ------------------------------- | -------------------------- | ---------------- | ------------- | ----------------- | --------------------------------- | ------------------------ | ---------- |
| 24    | Low level in reactor (general)  | Lower     | Level     | incorrect operation | low feed in reacor   |                                 | reduced amount of product  |                  |               |                   | install remote valves on the feed | install low level alarm  | Yang       |
| 25    | High level in reactor (general) | Higher    | Level     | incorrect operation | more feed in reactor | output valve incorrectly closed | high conversion in reactor | high temperature | \-            |                   | install remote valves on the feed | install high level alarm | Yang       |

#### Reactor for pressure
| Index | Description                        | Guideword | Parameter | Cause_1                                   | Cause_2                            | Cause_3                                | Consequence_1                                     | Consequence_2             | Consequence_3 | Danger of leakage | Safeguard_1                 | Safeguard_2                                        | References                                                             |
| ----- | ---------------------------------- | --------- | --------- | ----------------------------------------- | ---------------------------------- | -------------------------------------- | ------------------------------------------------- | ------------------------- | ------------- | ----------------- | --------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------- |
| 20    | High pressure in reactor (general) | Higher    | Pressure  | uncontrolled reaction occurs              | too much reactant into reactor     | too littel product flow out of reactor | reactor material could weaken                     | causing leak or explosion | \-            | Yes               | install high pressure alarm | install safety valve                               | Ciricillo [^7] |
| 21    | Low pressure in reactor (general)  | Lower     | Pressure  | too much product flow leaving the reactor | temperature dramatically decreases | \-                                     | uncontroll reactant and product flow into reactor | \-                        | \-            |                   | install pressure sensor     | add valve controls onto product and reactant lines | Ciricillo [^7] |

#### Reactor for temperature
| Index | Description                           | Guideword | Parameter   | Cause_1                                   | Cause_2                                                    | Cause_3 | Consequence_1                       | Consequence_2                   | Consequence_3 | Danger of leakage | Safeguard_1                | Safeguard_2                           | References                                                             |
| ----- | ------------------------------------- | --------- | ----------- | ----------------------------------------- | ---------------------------------------------------------- | ------- | ----------------------------------- | ------------------------------- | ------------- | ----------------- | -------------------------- | ------------------------------------- | ---------------------------------------------------------------------- |
| 22    | High temperature in reactor (general) | Higher    | Temperature | incoming reactant temperature is too high | reaction thermodynamics proceed in an uncontrolled fashion | \-      | reactor could overheat              | reactor pressure could increase | \-            |                   | install temperature sensor | add thermal control jacket to reactor | Ciricillo [^7] |
| 23    | Low temperature in reactor (general)  | Lower     | Temperature | incoming reactant temperature is too low  | heat jacket to reactor out                                 | \-      | reaction kinetics would be affected | reactor pressure could decrease | \-            |                   | install temperature sensor | add thermal control jacket to reactor |Ciricillo [^7] |

### Vessel
#### Vessel for flow
| Index | Description                                    | Guideword | Parameter | Cause_1         | Cause_2                  | Cause_3 | Consequence_1                | Consequence_2 | Consequence_3 | Danger of leakage | Safeguard_1                       | Safeguard_2 | References |
| ----- | ---------------------------------------------- | --------- | --------- | --------------- | ------------------------ | ------- | ---------------------------- | ------------- | ------------- | ----------------- | --------------------------------- | ----------- | ---------- |
| 32    | More flow from outlet pipe into tank (general) | Reverse   | Flow      | operation error | lower pressure in vessel | \-      | risk of overflow in the tank | \-            |               |                   | install check valve on the outlet | \-          | Yang       |

#### Vessel for level
| Index | Description                    | Guideword | Parameter | Cause_1       | Cause_2         | Cause_3                                                             | Consequence_1        | Consequence_2   | Consequence_3 | Danger of leakage | Safeguard_1              | Safeguard_2                                              | References                     |
| ----- | ------------------------------ | --------- | --------- | ------------- | --------------- | ------------------------------------------------------------------- | -------------------- | --------------- | ------------- | ----------------- | ------------------------ | -------------------------------------------------------- | ------------------------------ |
| 27    | High level in vessel (general) | Higher    | Level     | human error   | operation error | indicates the level in the vessel is almost twice the actual level. | overflow in the tank | risk of leakage | \-            | Yes               | install high level alarm | installation of more than one measurement for the vessel | Kletz [^1] and changed by Yang |
| 28    | Low level in vessel (general)  | Lower     | Level     | vessel defect | operation error |                                                                     | risk of leakage      | \-              | \-            | Yes               | install low level alarm  | \-                                                       | Yang                           |

#### Vessel for pressure
| Index | Description                       | Guideword | Parameter | Cause_1          | Cause_2                                  | Cause_3 | Consequence_1   | Consequence_2 | Consequence_3 | Danger of leakage | Safeguard_1                 | Safeguard_2          | References                     |
| ----- | --------------------------------- | --------- | --------- | ---------------- | ---------------------------------------- | ------- | --------------- | ------------- | ------------- | ----------------- | --------------------------- | -------------------- | ------------------------------ |
| 26    | High pressure in vessel (general) | Higher    | Pressure  | high Temperatur  | exothermic reaction in the vessel        | \-      | risk of leakage | burst         | \-            | Yes               | install high pressure alarm | install safety valve | Kletz [^1] and changed by Yang |
| 29    | Low pressure in vessel (general)  | Lower     | Pressure  | fire in the tank | the temperature in the vessel is too low | \-      | vessel defect   | \-            | \-            |                   | install pressure sensor     | \-                   | Yang                           |

#### Vessel for temperature
| Index | Description                          | Guideword | Parameter   | Cause_1                             | Cause_2                            | Cause_3 | Consequence_1    | Consequence_2             | Consequence_3 | Danger of leakage | Safeguard_1                | Safeguard_2                    | References |
| ----- | ------------------------------------ | --------- | ----------- | ----------------------------------- | ---------------------------------- | ------- | ---------------- | ------------------------- | ------------- | ----------------- | -------------------------- | ------------------------------ | ---------- |
| 30    | High temperature in vessel (general) | Higher    | Temperature | high temperature of feeding         | exothermic reaction in the vessel  | \-      | risk of leakage  | vessel defect             | \-            |                   | install temperature sensor | install high temperature alarm | Yang       |
| 31    | Low temperature in vessel (general)  | Lower     | Temperature | evaporation of the stored chemicals | low temperature of the environment | \-      | risk of freezing | change of product quality | \-            |                   | install temperature sensor | install low temperature alarm  | Yang       |

### Column
#### Column for flow
| Index | Description                                                               | Guideword | Parameter | Cause_1                                          | Cause_2                                                               | Cause_3                                 | Consequence_1                       | Consequence_2                       | Consequence_3 | Danger of leakage | Safeguard_1                                      | Safeguard_2               | References                                                                                                                                                       |
| ----- | ------------------------------------------------------------------------- | --------- | --------- | ------------------------------------------------ | --------------------------------------------------------------------- | --------------------------------------- | ----------------------------------- | ----------------------------------- | ------------- | ----------------- | ------------------------------------------------ | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 37    | No flow in the column (general)                                           | No        | Flow      | feed pump defective                              | low level alarm and control valve shut                                | tube leakages and blocking              | column dry out                      | no operation                        | \-            |                   | bypass                                           | install low level alarm   | Mazri [^8] |
| 40    | High relux flow in the distillation column (Column with bubble cap trays) | Higher    | Flow      | reflux control error                             | distillate valve incorrectly closed, distillate valve opening smaller | feed stream too high                    | rain in the column (Durchregnen)    | entrainment of liquid by steam flow | \-            |                   | independent reflux and distillate stream control | install feed flow control | Engell [^9], Yang                                                                                                                           |
| 41    | Low reflux flow in the distillation column (Column with bubble cap trays) | Lower     | Flow      | lower feed stream                                | lower condenser efficiency                                            | \-                                      | entrainment of liquid by steam flow | low purity of product               | \-            |                   | install flow rate control                        | check condenser           |  Engell [^9], Yang                                                                                                                           |
| 42    | No reflux flow in the distillation column (Column with bubble cap trays)  | No        | Flow      | heat exchanger for condensation not in operation | reflux flow control valve incorrectly closed                          | no feed flow in the distillation column | stop production                     | idling risk of the pump             | \-            |                   | check heat exchanger for condensation regularly  | check feed flow           | Yang                                                                                                                                                             |
| 45    | More feed to the distillation column (Column with bubble cap trays)       | Higher    | Flow      | human error                                      | wrong operation                                                       | \-                                      | overflow in the column              | risk of leakage                     | \-            |                   | install operation valve for feed                 | \-                        | Yang                                                                                                                                                             |
| 46    | Low feed to the  distillation column (Column with bubble cap trays)       | Lower     | Flow      | wrong operation                                  | feed pipe defect                                                      | feed blockage                           | risk of leakage                     | \-                                  | \-            |                   | install operation valve for feed                 | \-                        | Yang                                                                                                                                                             |

#### Column for level
| Index | Description                       | Guideword | Parameter | Cause_1               | Cause_2                            | Cause_3                    | Consequence_1              | Consequence_2                    | Consequence_3                                           | Danger of leakage | Safeguard_1              | Safeguard_2                     | References                                                                                                                                                       |
| ----- | --------------------------------- | --------- | --------- | --------------------- | ---------------------------------- | -------------------------- | -------------------------- | -------------------------------- | ------------------------------------------------------- | ----------------- | ------------------------ | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 38    | Less flow in the column (general) | Low       | Level     | pipe blockages        | low level alarm control valve shut | tube leakages and blocking | changes in product quality | possible dangerous concentration |                                                         |                   | bypass                   | install low level alarm         | Mazri [^8] |
| 39    | More flow in the column (general) | High      | Level     | control valve failure | increase pumping capacity          | low level alarm faulty     | flooding in the column     | changes in product quality       | increased corrosion and fouling of downstream equipment |                   | install high level alarm | install two independent control | Mazri [^8] |

#### Column for pressure
| Index | Description                                                 | Guideword | Parameter | Cause_1                                                                                                 | Cause_2                                              | Cause_3                                                 | Consequence_1                                 | Consequence_2                              | Consequence_3 | Danger of leakage | Safeguard_1                             | Safeguard_2                                        | References                        |
| ----- | ----------------------------------------------------------- | --------- | --------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------- | --------------------------------------------- | ------------------------------------------ | ------------- | ----------------- | --------------------------------------- | -------------------------------------------------- | --------------------------------- |
| 34    | High pressure in the column  (general)                      | Higher    | Pressure  | too long residence time due to operational disturbances                                                 | occurrence of an autocatalytic decomposition process | thermally unstable component being constricted too much | decomposition of substances                   | unexpected rise in temperature and presure | \-            |                   | install safety valve                    | install high pressure alarm                        | DECHEMA Ereignis-Datenbank        |
| 36    | Substance leakage due to corrosion of a weld seam (general) | Lower     | Pressure  | a high flow velocity in the area of the weld seam attacked the seam mechanically and chemical corrosion | \-                                                   | \-                                                      | leaks occurred in the area of the column sump | leak of product                            | \-            | Yes               | avoid weld seams in general if possible | reduce the flow velocity in the area of weld seams | DECHEMA [^4] + Yang |

#### Column for temperature
| Index | Description                                              | Guideword | Parameter   | Cause_1                                                 | Cause_2                                              | Cause_3                                                 | Consequence_1               | Consequence_2                              | Consequence_3 | Danger of leakage | Safeguard_1                                                                           | Safeguard_2                    | References                 |
| ----- | -------------------------------------------------------- | --------- | ----------- | ------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------- | --------------------------- | ------------------------------------------ | ------------- | ----------------- | ------------------------------------------------------------------------------------- | ------------------------------ | -------------------------- |
| 33    | Low temperature in the column (general)                  | Lower     | Temperature | low environmental temperature                           | lower feed temperature                               | \-                                                      | low purity of product       | \-                                         | \-            |                   | install low temperature alarm                                                         | \-                             | Yang                       |
| 35    | High temperature in the column (general)                 | Higer     | Temperature | too long residence time due to operational disturbances | occurrence of an autocatalytic decomposition process | thermally unstable component being constricted too much | decomposition of substances | unexpected rise in temperature and presure | \-            |                   | DTA measurements of the input mixture and the concentrated residue and the distillate | install high temperature alarm | DECHEMA [^4] |
| 43    | Feed temperature too low (Column with bubble cap trays)  | Lower     | Temperature | wrong operation                                         | \-                                                   | \-                                                      | low purity of product       | \-                                         | \-            |                   | install temperature sensor for feed                                                   | \-                             | Yang                       |
| 44    | Feed temperature too high (Column with bubble cap trays) | Higher    | Temperature | wrong operation                                         | \-                                                   | \-                                                      | loss of light component     | high pressure in the column                | \-            |                   | install temperature sensor for feed                                                   | \-                             | Yang                       |

References: 
[^1]: Kletz, T. What went wrong? Case histories of process plant disasters and how they could have been avoided, 5th ed.; Gulf Professional: Burlington, MA, 2009.
[^2]: Zennir, Y.; Bendib, R. The dependability control analysis: Applied to centrifugal pumps in a oil petrochemical plant. In 2015 International Conference on Industrial Engineering and Systems Management (IESM); IEEE, 2015; pp 1004–1011.
[^3]: Holtermann, T. Entwicklung eines Expertentools zur automatisierten Sicherheitsbetrachtung von standardisierten R&I-Fließbildern im DEXPI Format. Masterarbeit; Technische Universität Dortmund, Dortmund, 2022.
[^4]: ProcessNet Ereignis-Datenbank, online documentation, https://processnet.org/ereignisdb.html, accessed on 22.04.2023
[^5]: Learn about centrifugal water pump idling, online documentation, https://angroupcn.com/learn-about-centrifugal-water-pump-idling/, accessed on 22.04.2023
[^6]: Hazard and Operability (HAZOP), online documentation, https://www.ehsdb.com/hazop.php, accessed on 22.04.2023
[^7]:  Ciricillo, S. Hazard and Operability Analysis of an Ethylene Oxide Production Plant, online documentation, https://scholarcommons.sc.edu/cgi/viewcontent.cgi?article=1276&context=senior_theses, accessed on 22.04.2023
[^8]: HAZOP for Distillation column Parameter Guideword Deviation Possible Cause Consequence Action, online documentation, https://www.academia.edu/33328920/HAZOP_for_Distillation_column_Parameter_Guideword_Deviation_Possible_Cause_Consequence_Action_Flow_NO_No_flow_at_BULLET_Pipe_blockages, accessed on 22.04.2023
[^9]: Engell, S; Goerke, T. Vorlesung Prozessautomatisierung: Vorlesung 8 Reglerstrukturauswahl / Prozessmanagement, WS 19/20